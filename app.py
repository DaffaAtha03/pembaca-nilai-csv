from __future__ import annotations

import html
import io
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from i18n import LANGS, tr

BASE = Path(__file__).parent

st.set_page_config(page_title="CSV Quality Checker", page_icon="🔎", layout="wide")
st.markdown(f"<style>{(BASE / 'style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


# ---------------------------------------------------------------- bahasa
head_left, head_right = st.columns([5, 2])
with head_right:
    if hasattr(st, "segmented_control"):
        choice = st.segmented_control(
            "Language", list(LANGS), format_func=LANGS.get, default="id",
            key="lang_sel", label_visibility="collapsed",
        )
        lang = choice or "id"
    else:
        lang = st.radio("Language", list(LANGS), format_func=LANGS.get,
                        horizontal=True, key="lang_sel", label_visibility="collapsed")


def t(key: str, **kwargs) -> str:
    return tr(lang, key, **kwargs)


with head_left:
    st.markdown(
        f"""
        <div class="hero">
          <div class="mark"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
          <div><h1>{html.escape(t('title'))}</h1><p>{html.escape(t('subtitle'))}</p></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------- data
@st.cache_data(show_spinner=False)
def load_csv(raw: bytes) -> pd.DataFrame:
    """Baca CSV; pemisah (koma/titik koma/tab) dan encoding dideteksi otomatis."""
    last_error: Exception | None = None
    for encoding in ("utf-8-sig", "latin-1"):
        try:
            return pd.read_csv(io.BytesIO(raw), sep=None, engine="python", encoding=encoding)
        except UnicodeDecodeError as exc:
            last_error = exc
    raise last_error  # type: ignore[misc]


def sample_df() -> pd.DataFrame:
    cities = ["Jakarta", "Bekasi", "Bandung", "Surabaya", "Medan"]
    rows = [
        {
            "id": i,
            "nama": f"Pelanggan {i}",
            "kota": cities[i % 5] if i % 9 else None,
            "usia": 18 + (i * 7) % 45 if i % 11 else None,
            "total_belanja": 50_000 + (i * 13_731) % 950_000,
            "status": "aktif",
        }
        for i in range(1, 121)
    ]
    df = pd.DataFrame(rows)
    return pd.concat([df, df.iloc[:6]], ignore_index=True)


def severity(pct: float) -> str:
    return "bad" if pct >= 50 else "warn" if pct >= 20 else "ok"


def analyse(df: pd.DataFrame) -> dict:
    n_rows, n_cols = df.shape
    missing = df.isna().sum()
    dup_mask = df.duplicated()
    cells = n_rows * n_cols
    unique_counts = {c: int(df[c].nunique(dropna=True)) for c in df.columns}
    constant = [c for c, n in unique_counts.items() if n <= 1]

    completeness = 1 - int(missing.sum()) / cells if cells else 1.0
    uniqueness = 1 - int(dup_mask.sum()) / n_rows if n_rows else 1.0
    variety = 1 - len(constant) / n_cols if n_cols else 1.0
    score = round(100 * (0.5 * completeness + 0.3 * uniqueness + 0.2 * variety))

    return {
        "rows": n_rows, "cols": n_cols, "missing": missing,
        "total_missing": int(missing.sum()), "dup_mask": dup_mask,
        "dups": int(dup_mask.sum()), "unique_counts": unique_counts,
        "constant": constant, "score": score,
        "parts": {"b_complete": completeness, "b_unique": uniqueness, "b_variety": variety},
    }


def bar_html(filled_pct: float, level: str) -> str:
    cls = "" if level == "ok" else level
    return f'<div class="bar"><div class="{cls}" style="width:{max(0, min(100, filled_pct)):.1f}%"></div></div>'


def verdict(score: int) -> tuple[str, str]:
    if score >= 85:
        return t("verdict_good"), "#0F9D7A"
    if score >= 65:
        return t("verdict_ok"), "#B87F00"
    return t("verdict_bad"), "#D63A42"


# ---------------------------------------------------------------- input
uploaded = st.file_uploader(t("upload"), type=["csv"])
st.markdown(f'<div class="privacy">{html.escape(t("privacy"))}</div>', unsafe_allow_html=True)

if uploaded is not None:
    st.session_state["use_sample"] = False
elif st.button(t("sample_btn")):
    st.session_state["use_sample"] = True

df: pd.DataFrame | None = None
source_name = ""

if uploaded is not None:
    try:
        df = load_csv(uploaded.getvalue())
        source_name = uploaded.name
    except Exception as exc:  # noqa: BLE001 - tampilkan pesan ramah ke pengguna
        st.error(t("read_error", err=exc))
        st.stop()
elif st.session_state.get("use_sample"):
    df = sample_df()
    source_name = "sample_data.csv"

if df is None:
    st.markdown(
        f'<div class="empty"><h3>{html.escape(t("empty_title"))}</h3>'
        f'<div>{html.escape(t("empty_body"))}</div></div>',
        unsafe_allow_html=True,
    )
    st.stop()

if df.empty:
    st.warning(t("empty_df"))
    st.stop()

# ---------------------------------------------------------------- analisis
a = analyse(df)
rows_text, cols_text = f"{a['rows']:,}", f"{a['cols']:,}"
loaded_text = t("loaded", name=source_name, rows=rows_text, cols=cols_text)
st.markdown(f'<div class="loaded">{html.escape(loaded_text)}</div>', unsafe_allow_html=True)

label, color = verdict(a["score"])
gauge = (
    (BASE / "gauge.html").read_text(encoding="utf-8")
    .replace("{{SCORE}}", str(a["score"]))
    .replace("{{COLOR}}", color)
    .replace("{{TITLE}}", html.escape(t("score_title")))
    .replace("{{VERDICT}}", html.escape(label))
)

left, right = st.columns([5, 7], gap="large")
with left:
    components.html(gauge, height=214)
with right:
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(t("m_rows"), f"{a['rows']:,}")
    m2.metric(t("m_cols"), f"{a['cols']:,}")
    m3.metric(t("m_missing"), f"{a['total_missing']:,}")
    m4.metric(t("m_dups"), f"{a['dups']:,}")
    rows_html = "".join(
        f'<div class="bd-row"><span>{html.escape(t(k))}</span>'
        f'{bar_html(v * 100, "ok" if v >= .95 else "warn" if v >= .8 else "bad")}'
        f'<span>{v * 100:.0f}%</span></div>'
        for k, v in a["parts"].items()
    )
    st.markdown(f'<div class="breakdown">{rows_html}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------- tab
tab_overview, tab_columns, tab_preview, tab_dups = st.tabs(
    [t("tab_overview"), t("tab_columns"), t("tab_preview"), t("tab_dups")]
)

summary = pd.DataFrame({
    t("c_name"): df.columns,
    t("c_type"): [str(d) for d in df.dtypes],
    t("c_missing"): [int(a["missing"][c]) for c in df.columns],
    t("c_pct"): [round(float(a["missing"][c] / a["rows"] * 100), 2) for c in df.columns],
    t("c_unique"): [a["unique_counts"][c] for c in df.columns],
})

with tab_overview:
    st.subheader(t("findings"))
    findings: list[tuple[str, str]] = []
    for c in df.columns:
        pct = float(a["missing"][c] / a["rows"] * 100)
        if pct >= 20:
            findings.append((severity(pct), t("f_missing", col=c, pct=f"{pct:.1f}")))
    for c in a["constant"]:
        findings.append(("warn", t("f_constant", col=c)))
    if a["dups"]:
        level = "bad" if a["dups"] / a["rows"] >= 0.1 else "warn"
        findings.append((level, t("f_dups", n=f"{a['dups']:,}")))
    if not findings:
        findings = [("ok", t("no_findings"))]
    st.markdown(
        "".join(f'<div class="finding {lv}"><span class="dot"></span><span>{html.escape(msg)}</span></div>'
                for lv, msg in findings),
        unsafe_allow_html=True,
    )

    st.subheader(t("col_health"))
    col_rows = "".join(
        f'<div class="colrow"><span class="name" title="{html.escape(str(c))}">{html.escape(str(c))}</span>'
        f'{bar_html(100 - float(a["missing"][c] / a["rows"] * 100), severity(float(a["missing"][c] / a["rows"] * 100)))}'
        f'<span class="pct">{100 - float(a["missing"][c] / a["rows"] * 100):.1f}%</span></div>'
        for c in df.columns
    )
    st.markdown(f'<div class="panel">{col_rows}</div>', unsafe_allow_html=True)

with tab_columns:
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.download_button(
        t("dl_report"), summary.to_csv(index=False).encode("utf-8"),
        file_name="column_report.csv", mime="text/csv",
    )

with tab_preview:
    st.caption(t("preview_note"))
    st.dataframe(df.head(100), use_container_width=True)

with tab_dups:
    if a["dups"] == 0:
        st.markdown(f'<div class="finding ok"><span class="dot"></span><span>{html.escape(t("dups_none"))}</span></div>',
                    unsafe_allow_html=True)
    else:
        st.caption(t("dups_info", n=f"{a['dups']:,}"))
        st.dataframe(df[a["dup_mask"]].head(200), use_container_width=True)
        st.download_button(
            t("dl_clean"), df.drop_duplicates().to_csv(index=False).encode("utf-8"),
            file_name="data_no_duplicates.csv", mime="text/csv",
        )

with st.expander(t("how_title")):
    st.markdown(t("how_body"))
