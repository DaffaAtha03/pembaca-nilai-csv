"""Teks antarmuka dalam beberapa bahasa. Tambah bahasa baru = tambah satu blok di TEXT."""

LANGS = {"id": "Indonesia", "en": "English", "zh": "中文"}

TEXT = {
    "id": {
        "title": "Pemeriksa Kualitas CSV",
        "subtitle": "Unggah CSV dan lihat seberapa siap datanya untuk dianalisis.",
        "upload": "Unggah file CSV",
        "sample_btn": "Pakai data contoh",
        "privacy": "File hanya diproses selama sesi ini dan tidak disimpan oleh aplikasi.",
        "empty_title": "Belum ada data",
        "empty_body": "Unggah file CSV di atas, atau pakai data contoh untuk melihat cara kerjanya.",
        "read_error": "File tidak bisa dibaca sebagai CSV. Periksa formatnya. Detail: {err}",
        "empty_df": "File terbaca, tetapi tidak ada baris data.",
        "loaded": "{name}: {rows} baris, {cols} kolom",
        "m_rows": "Baris",
        "m_cols": "Kolom",
        "m_missing": "Nilai kosong",
        "m_dups": "Baris duplikat",
        "score_title": "Skor kesehatan data",
        "verdict_good": "Siap dianalisis",
        "verdict_ok": "Perlu dibersihkan",
        "verdict_bad": "Banyak masalah",
        "b_complete": "Kelengkapan",
        "b_unique": "Keunikan baris",
        "b_variety": "Variasi kolom",
        "tab_overview": "Ringkasan",
        "tab_columns": "Kolom",
        "tab_preview": "Pratinjau",
        "tab_dups": "Duplikat",
        "findings": "Temuan",
        "no_findings": "Tidak ada masalah besar yang terdeteksi.",
        "f_missing": "Kolom «{col}» kosong {pct}%.",
        "f_constant": "Kolom «{col}» hanya berisi satu nilai atau kosong semua.",
        "f_dups": "{n} baris duplikat penuh.",
        "col_health": "Kelengkapan per kolom",
        "c_name": "nama_kolom",
        "c_type": "tipe_data",
        "c_missing": "nilai_kosong",
        "c_pct": "persentase_kosong",
        "c_unique": "nilai_unik",
        "dl_report": "Unduh laporan kolom (CSV)",
        "dl_clean": "Unduh data tanpa duplikat (CSV)",
        "preview_note": "Menampilkan 100 baris pertama.",
        "dups_none": "Tidak ada baris duplikat penuh.",
        "dups_info": "{n} baris yang sama persis dengan baris sebelumnya (maks. 200 ditampilkan).",
        "how_title": "Cara skor dihitung",
        "how_body": (
            "**Skor = 50% kelengkapan + 30% keunikan baris + 20% variasi kolom.**\n\n"
            "- **Kelengkapan:** porsi sel yang terisi.\n"
            "- **Keunikan baris:** porsi baris yang bukan duplikat penuh.\n"
            "- **Variasi kolom:** porsi kolom yang punya lebih dari satu nilai.\n\n"
            "Duplikat parsial (berdasarkan kolom tertentu) belum diperiksa."
        ),
    },
    "en": {
        "title": "CSV Quality Checker",
        "subtitle": "Upload a CSV and see how ready it is for analysis.",
        "upload": "Upload a CSV file",
        "sample_btn": "Use sample data",
        "privacy": "Files are processed only during this session and are not stored by the app.",
        "empty_title": "No data yet",
        "empty_body": "Upload a CSV file above, or use the sample data to see how it works.",
        "read_error": "This file could not be read as CSV. Check its format. Details: {err}",
        "empty_df": "The file was read, but it has no data rows.",
        "loaded": "{name}: {rows} rows, {cols} columns",
        "m_rows": "Rows",
        "m_cols": "Columns",
        "m_missing": "Missing values",
        "m_dups": "Duplicate rows",
        "score_title": "Data health score",
        "verdict_good": "Ready to analyse",
        "verdict_ok": "Needs cleaning",
        "verdict_bad": "Many problems",
        "b_complete": "Completeness",
        "b_unique": "Row uniqueness",
        "b_variety": "Column variety",
        "tab_overview": "Overview",
        "tab_columns": "Columns",
        "tab_preview": "Preview",
        "tab_dups": "Duplicates",
        "findings": "Findings",
        "no_findings": "No major problems detected.",
        "f_missing": "Column “{col}” is {pct}% empty.",
        "f_constant": "Column “{col}” has a single value or is entirely empty.",
        "f_dups": "{n} fully duplicated rows.",
        "col_health": "Completeness by column",
        "c_name": "column",
        "c_type": "dtype",
        "c_missing": "missing",
        "c_pct": "missing_pct",
        "c_unique": "unique",
        "dl_report": "Download column report (CSV)",
        "dl_clean": "Download data without duplicates (CSV)",
        "preview_note": "Showing the first 100 rows.",
        "dups_none": "No fully duplicated rows.",
        "dups_info": "{n} rows identical to an earlier row (up to 200 shown).",
        "how_title": "How the score is calculated",
        "how_body": (
            "**Score = 50% completeness + 30% row uniqueness + 20% column variety.**\n\n"
            "- **Completeness:** share of cells that are filled.\n"
            "- **Row uniqueness:** share of rows that are not full duplicates.\n"
            "- **Column variety:** share of columns with more than one value.\n\n"
            "Partial duplicates (on specific columns) are not checked yet."
        ),
    },
    "zh": {
        "title": "CSV 数据质量检查器",
        "subtitle": "上传 CSV，看看数据是否已经可以用于分析。",
        "upload": "上传 CSV 文件",
        "sample_btn": "使用示例数据",
        "privacy": "文件仅在本次会话中处理，应用不会保存。",
        "empty_title": "还没有数据",
        "empty_body": "请在上方上传 CSV 文件，或使用示例数据体验。",
        "read_error": "无法将该文件读取为 CSV，请检查格式。详情：{err}",
        "empty_df": "文件已读取，但没有数据行。",
        "loaded": "{name}：{rows} 行，{cols} 列",
        "m_rows": "行数",
        "m_cols": "列数",
        "m_missing": "缺失值",
        "m_dups": "重复行",
        "score_title": "数据健康评分",
        "verdict_good": "可以开始分析",
        "verdict_ok": "需要清理",
        "verdict_bad": "问题较多",
        "b_complete": "完整度",
        "b_unique": "行唯一性",
        "b_variety": "列多样性",
        "tab_overview": "概览",
        "tab_columns": "列",
        "tab_preview": "预览",
        "tab_dups": "重复项",
        "findings": "发现",
        "no_findings": "未发现严重问题。",
        "f_missing": "列“{col}”有 {pct}% 为空。",
        "f_constant": "列“{col}”只有一个值或全部为空。",
        "f_dups": "有 {n} 行完全重复。",
        "col_health": "各列完整度",
        "c_name": "列名",
        "c_type": "数据类型",
        "c_missing": "缺失数",
        "c_pct": "缺失比例",
        "c_unique": "唯一值数",
        "dl_report": "下载列报告 (CSV)",
        "dl_clean": "下载去重后的数据 (CSV)",
        "preview_note": "显示前 100 行。",
        "dups_none": "没有完全重复的行。",
        "dups_info": "有 {n} 行与前面的行完全相同（最多显示 200 行）。",
        "how_title": "评分如何计算",
        "how_body": (
            "**评分 = 50% 完整度 + 30% 行唯一性 + 20% 列多样性。**\n\n"
            "- **完整度：** 已填写单元格的比例。\n"
            "- **行唯一性：** 不是完全重复的行的比例。\n"
            "- **列多样性：** 取值多于一个的列的比例。\n\n"
            "暂不检查按特定列判断的部分重复。"
        ),
    },
}


def tr(lang: str, key: str, **kwargs) -> str:
    text = TEXT.get(lang, TEXT["id"]).get(key) or TEXT["id"][key]
    return text.format(**kwargs) if kwargs else text
