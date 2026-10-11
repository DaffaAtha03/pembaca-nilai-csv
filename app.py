import pandas as pd
import streamlit as st

st.set_page_config(page_title="CSV Data Quality Checker", page_icon="🔎", layout="wide")

st.title("🔎 CSV Data Quality Checker")
st.write("Periksa kualitas dataset CSV sebelum digunakan untuk analisis.")

uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as exc:
        st.error(f"File tidak dapat dibaca. Periksa format CSV-nya. Detail: {exc}")
        st.stop()

    if df.empty:
        st.warning("File berhasil dibaca, tetapi tidak memiliki baris data.")
    else:
        st.success("File CSV berhasil dibaca.")

    total_rows, total_columns = df.shape
    total_missing = int(df.isna().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    missing_by_column = df.isna().sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jumlah baris", f"{total_rows:,}")
    col2.metric("Jumlah kolom", f"{total_columns:,}")
    col3.metric("Nilai kosong", f"{total_missing:,}")
    col4.metric("Baris duplikat", f"{duplicate_rows:,}")

    st.subheader("Pratinjau data")
    st.dataframe(df.head(100), use_container_width=True)

    st.subheader("Ringkasan kolom")
    summary = pd.DataFrame({
        "nama_kolom": df.columns,
        "tipe_data": [str(dtype) for dtype in df.dtypes],
        "nilai_kosong": [int(missing_by_column[col]) for col in df.columns],
        "persentase_kosong": [
            round(float(missing_by_column[col] / len(df) * 100), 2) if len(df) else 0
            for col in df.columns
        ],
        "nilai_unik": [int(df[col].nunique(dropna=True)) for col in df.columns],
    })
    st.dataframe(summary, use_container_width=True)

    st.subheader("Unduh laporan")
    report = summary.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Unduh laporan kualitas data (CSV)",
        data=report,
        file_name="laporan_kualitas_data.csv",
        mime="text/csv",
    )

    with st.expander("Apa arti hasil ini?"):
        st.write("- **Nilai kosong:** sel yang tidak memiliki nilai.")
        st.write("- **Baris duplikat:** baris yang seluruh nilainya sama dengan baris lain.")
        st.write("- **Nilai unik:** jumlah nilai berbeda pada setiap kolom, tanpa menghitung nilai kosong.")
        st.caption("Catatan: duplikasi parsial berdasarkan kolom tertentu belum diperiksa oleh versi awal ini.")
else:
    st.info("Mulai dengan mengunggah file CSV. Kamu juga bisa mencoba file sample_data.csv di repositori ini.")
