import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Fungsi untuk menghitung cosine similarity antara dua embedding
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Fungsi untuk memproses pertanyaan dan mencocokkan dengan embedding dokumen
def find_most_relevant_page(embeddings_file, question, model, threshold=0.5):
    # Load embedding dokumen dari file JSON
    with open(embeddings_file, 'r') as f:
        doc_embeddings = json.load(f)

    # Hasilkan embedding untuk pertanyaan menggunakan model yang sama
    question_embedding = model.encode(question)

    # Variabel untuk menyimpan halaman yang paling relevan
    best_page = None
    best_similarity = -1
    best_text = ""

    # Lakukan perbandingan embedding menggunakan cosine similarity
    for page in doc_embeddings:
        page_embedding = np.array(page['embeddings'])  # Ambil embedding dari dokumen
        similarity = cosine_similarity(question_embedding, page_embedding)
        
        if similarity > best_similarity:
            best_similarity = similarity
            best_page = page['page']
            best_text = page['text']

    # Cek apakah cosine similarity cukup tinggi (di atas threshold)
    if best_similarity < threshold:
        return None, None, best_similarity  # Tidak ada hasil yang relevan

    # Tampilkan hasil: halaman yang paling relevan dan teks yang sesuai
    return best_page, best_text, best_similarity

# Fungsi utama untuk memproses pertanyaan
def process_question(embeddings_file, question):
    # Load model sentence transformer
    model = SentenceTransformer('intfloat/multilingual-e5-large')  # Menggunakan model yang sama untuk embedding

    # Temukan halaman dan teks yang paling relevan dengan pertanyaan
    page, text, similarity = find_most_relevant_page(embeddings_file, question, model)

    # Handler jika tidak ada hasil relevan atau terlalu rendah similarity-nya
    if page is None:
        print(f"Maaf, tidak ada informasi yang relevan dengan pertanyaan Anda. Cosine similarity: {similarity:.2f}")
    else:
        print(f"Hasil terbaik ditemukan di halaman: {page} dengan cosine similarity: {similarity:.2f}")
        print(f"Teks yang relevan: {text}")

# Jalankan proses
embeddings_file = "nama_file.json"  # File JSON hasil embedding sebelumnya
question = "Kapan sertifikat keluar di dashboard prakerja?"  # Contoh pertanyaan dari pengguna
process_question(embeddings_file, question)
