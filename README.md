# Text Embedding dan Pencocokan Similaritas

Proyek ini mendemonstrasikan bagaimana mengekstrak embedding teks dari file PDF dan menemukan halaman dokumen yang paling relevan berdasarkan pertanyaan pengguna menggunakan cosine similarity. Proyek ini terdiri dari dua skrip utama: `prep.py` dan `main.py`.

- `prep.py`: Mengekstrak teks dari file PDF, menghasilkan embedding, dan menyimpannya dalam file JSON.
- `main.py`: Memuat file JSON, memproses pertanyaan pengguna, dan mengembalikan halaman dokumen yang paling relevan menggunakan cosine similarity.

## Prasyarat

Pastikan kamu sudah menginstal Python versi 3.7 atau lebih tinggi.

## Instalasi

1. Clone repository ini ke komputer lokal:
   ```bash
   git clone https://github.com/fataelislami/Text-Embedding.git
   cd Text-Embedding

2. Instal semua dependensi yang dibutuhkan menggunakan pip. Disarankan untuk menggunakan virtual environment untuk mengelola dependensi:

    ```bash
    python -m venv env  # Membuat virtual environment
    source env/bin/activate  # Mengaktifkan virtual environment (untuk macOS/Linux)
    # atau
    .\env\Scripts\activate  # Mengaktifkan virtual environment (untuk Windows)

    pip install -r requirements.txt  # Instal semua dependensi dari file requirements.txt
