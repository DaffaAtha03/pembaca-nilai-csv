# CSV Data Quality Checker

Aplikasi sederhana berbasis Python dan Streamlit untuk memeriksa kualitas dataset CSV.

## Fitur
- Upload file CSV
- Menampilkan jumlah baris dan kolom
- Menghitung nilai kosong
- Menghitung baris duplikat penuh
- Merangkum tipe data dan jumlah nilai unik
- Mengunduh laporan ringkasan dalam format CSV

## Teknologi
- Python
- Pandas
- Streamlit

## Menjalankan aplikasi secara lokal

1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder proyek.
3. Buat virtual environment (disarankan):

   ```bash
   python -m venv .venv
   ```

4. Aktifkan virtual environment:

   Windows:
   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

5. Instal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi:

   ```bash
   streamlit run app.py
   ```

## Struktur proyek

```text
csv-data-quality-checker/
├── app.py
├── requirements.txt
├── README.md
└── sample_data.csv
```

## Ide pengembangan berikutnya
- Menambahkan pilihan kolom untuk memeriksa duplikasi
- Menambahkan grafik kualitas data
- Menambahkan ekspor laporan ke Excel
- Menambahkan validasi tipe data dan rentang nilai
- Menambahkan pengujian otomatis
- Menambahkan integrasi AI untuk menjelaskan temuan, dengan hasil tetap diverifikasi dari data

## Batasan
Versi awal ini memeriksa duplikasi berdasarkan kesamaan seluruh kolom. Data tidak secara otomatis dibersihkan atau diubah.

## link file
https://pembaca-nilai-csv-daffathr.streamlit.app/
