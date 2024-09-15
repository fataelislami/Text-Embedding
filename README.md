# Text Embedding dan Pencocokan Similaritas

Proyek ini mendemonstrasikan bagaimana mengekstrak embedding teks dari file PDF dan menemukan halaman dokumen yang paling relevan berdasarkan pertanyaan pengguna menggunakan cosine similarity. Proyek ini terdiri dari dua skrip utama: `prep.py` dan `main.py`.

- `prep.py`: Mengekstrak teks dari file PDF, menghasilkan embedding, dan menyimpannya dalam file JSON.
- `main.py`: Memuat file JSON, memproses pertanyaan pengguna, dan mengembalikan halaman dokumen yang paling relevan menggunakan cosine similarity.

## Prasyarat

Python versi 3.7 atau lebih tinggi.

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

# Panduan Penggunaan EmbedMatcher

## Langkah-langkah Menjalankan

### 1. Membuat Embedding dari PDF (Jalankan `prep.py`)
Langkah pertama adalah mengekstrak teks dari file PDF dan menghasilkan embedding teks. Kamu perlu mengubah variabel `pdf_file_path` dan `output_json_path` di dalam file `prep.py` sesuai dengan lokasi file PDF dan nama file JSON yang diinginkan.

Untuk menjalankan skrip:

```bash
python prep.py
```

Skrip ini akan membaca file PDF, menghasilkan embedding untuk setiap halaman, dan menyimpan hasilnya dalam file JSON.

### 2. Proses Pertanyaan Pengguna dan Cek Similaritas (Jalankan `main.py`)
Setelah menghasilkan embedding, kamu bisa menjalankan skrip `main.py` untuk memproses pertanyaan pengguna. Pastikan variabel `embeddings_file` di dalam `main.py` mengarah ke file JSON yang dihasilkan oleh `prep.py`.

Untuk menjalankan skrip:

```bash
python main.py
```

Skrip ini akan menerima pertanyaan pengguna (misalnya, "Kapan Indonesia Merdeka?"), dan mengembalikan halaman yang paling relevan berdasarkan cosine similarity.

## File-File

- `main.py`: Berisi kode untuk memproses pertanyaan pengguna dan menghitung cosine similarity.
- `prep.py`: Berisi kode untuk mengekstrak teks dari PDF dan menghasilkan embedding teks.
- `requirements.txt`: Daftar paket Python yang diperlukan.

## Dependensi

Proyek ini menggunakan beberapa library Python:

- `numpy`: Untuk operasi matematika seperti cosine similarity.
- `sentence-transformers`: Untuk menghasilkan embedding teks.
- `pymupdf (fitz)`: Untuk mengekstrak teks dari file PDF.

## Catatan

- Kamu akan membutuhkan file PDF untuk menghasilkan embedding pada langkah pertama. Pastikan path ke file PDF sudah benar diatur dalam variabel `pdf_file_path` di `prep.py`.
- Model yang digunakan untuk menghasilkan embedding adalah `intfloat/multilingual-e5-large`. Kamu bisa mengganti model ini dengan model lain jika diperlukan dengan mengubah parameter `model` di kedua skrip.

## Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
