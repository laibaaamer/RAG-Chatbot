import os
import time
from pathlib import Path
import chromadb
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google import genai
from google.genai import errors as genai_errors
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env")
BASE_DIR = Path(__file__).resolve().parent
VECTOR_DB_DIR = BASE_DIR / "vector_db"
COLLECTION_NAME = "knowledge_base"
MODEL = "gemini-3.6-flash"
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
client = genai.Client(api_key=GEMINI_API_KEY)
chroma_client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))
collection = chroma_client.get_collection(name=COLLECTION_NAME)
def retrieve_context(question, top_k=3):
    query_embedding = embedding_model.encode(question).tolist()
    results = collection.query(query_embeddings=[query_embedding],n_results=top_k)
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    return documents, metadatas
def format_chat_history(chat_history):
    if not chat_history:
        return "No previous conversation."
    history_text = ""
    recent_history = chat_history[-6:]
    for message in recent_history:
        role = message["role"].capitalize()
        content = message["content"]
        history_text += (f"{role}: {content}\n")
    return history_text
def generate_answer(question,documents,chat_history=None,max_retries=4):
    context = "\n\n".join(documents)
    history = format_chat_history(chat_history)
    prompt = f"""
You are a helpful AI assistant.
Answer the user's question using ONLY the
provided knowledge-base context.
You also have access to the previous conversation
to understand follow-up questions and references.
If the answer cannot be found in the knowledge-base
context, say:
"I couldn't find this information in the
knowledge base."
Do not invent information.
Previous Conversation:
-----------------------
{history}
-----------------------
Knowledge Base Context:
-----------------------
{context}
-----------------------
Current User Question:
{question}
Answer clearly and concisely while considering
the previous conversation when understanding
the user's question.
"""
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(model=MODEL,contents=prompt)
            return response.text
        except genai_errors.ServerError as e:
            if getattr(e, "code", None) == 503:
                wait_time = 2 ** attempt
                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise
    return (
        "Gemini is temporarily unavailable. "
        "Please try again in a few moments.")
def ask_question(question,chat_history=None):
    history_text = format_chat_history(chat_history)
    retrieval_query = f"""
Previous conversation:
{history_text}
Current question:
{question}
"""
    documents, metadatas = retrieve_context(retrieval_query)
    answer = generate_answer(question,documents,chat_history)
    sources = [
        f"Page {metadata.get('page', 'N/A')}"
        for metadata in metadatas]
    return answer, sources, documents