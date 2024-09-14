import re
import fitz  # PyMuPDF
import json
from sentence_transformers import SentenceTransformer

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Menghapus karakter non-alfanumerik kecuali spasi
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    # Menghapus spasi berlebih, tab, atau newline yang tidak perlu
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Fungsi untuk membaca file PDF dan menghasilkan teks per halaman
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages_text = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        # clean = clean_text(text)  # Bersihkan teks
        pages_text.append({"page": page_num + 1, "text": text})
    return pages_text

# Fungsi untuk menghasilkan embedding dari teks
def generate_embeddings(texts, model):
    embeddings = []
    for text in texts:
        # Menghasilkan embedding dari teks
        embedding = model.encode(text['text'])
        text['embeddings'] = embedding.tolist()  # Konversi embedding ke list agar bisa disimpan ke JSON
    return texts

# Fungsi untuk menyimpan hasil embedding ke dalam file JSON
def save_to_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

# Main function
def process_pdf(pdf_path, output_json_path):
    # Load model sentence transformer
    model = SentenceTransformer('intfloat/multilingual-e5-large')  # Menggunakan model embedding

    # Ekstraksi teks dari PDF
    pages_text = extract_text_from_pdf(pdf_path)

    # Menghasilkan embedding dari teks per halaman
    pages_with_embeddings = generate_embeddings(pages_text, model)

    # Simpan hasil ke dalam file JSON
    save_to_json(pages_with_embeddings, output_json_path)

# Jalankan proses
pdf_file_path = "nama_file.pdf"  # Ganti dengan path file PDF yang kamu upload
output_json_path = "nama_file.json"  # Nama file output
process_pdf(pdf_file_path, output_json_path)

print(f"Hasil embedding disimpan dalam {output_json_path}")
