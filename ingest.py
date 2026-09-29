from pathlib import Path
import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"
VECTOR_DB_DIR = BASE_DIR / "vector_db"
PDF_PATH = DOCUMENTS_DIR / "knowledge_base.pdf"
COLLECTION_NAME = "knowledge_base"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    documents = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            documents.append({
                "text": text,
                "page": page_number})
    return documents
def create_chunks(text, page_number):
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end].strip()
        if chunk:
            chunks.append({
                "text": chunk,
                "page": page_number})
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks
def main():
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")
    print("Loading PDF...")
    pages = load_pdf(PDF_PATH)
    print(f"Pages loaded: {len(pages)}")
    all_chunks = []
    for page in pages:
        page_chunks = create_chunks(
            page["text"],
            page["page"])
        all_chunks.extend(page_chunks)
    print(f"Total chunks: {len(all_chunks)}")
    print("Generating embeddings...")
    texts = [
        chunk["text"]
        for chunk in all_chunks]
    embeddings = embedding_model.encode(
        texts,
        show_progress_bar=True)
    print("Creating ChromaDB...")
    chroma_client = chromadb.PersistentClient(
        path=str(VECTOR_DB_DIR)
    )
    try:
        chroma_client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = chroma_client.create_collection(name=COLLECTION_NAME)
    ids = [
        f"chunk_{i}"
        for i in range(len(all_chunks))]
    metadatas = [
        {"page": chunk["page"]}
        for chunk in all_chunks]
    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas)
    print(f"Documents stored: {len(texts)}")
if __name__ == "__main__":
    main()