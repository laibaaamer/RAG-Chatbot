# 🤖 RAG AI Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG) chatbot** that answers questions from a company knowledge base. The application retrieves relevant information from documents using semantic search and generates contextual responses using the **Gemini API**.

The chatbot is built with **Python, Streamlit, ChromaDB, Sentence Transformers, and Gemini**.

---

## 🚀 Features

* 📚 **Knowledge Base Q&A** — Answers questions using information from the uploaded knowledge base.
* 🔎 **Semantic Search** — Uses Sentence Transformers to generate embeddings and retrieve relevant document chunks.
* 🗄️ **ChromaDB** — Stores and searches document embeddings efficiently.
* 🤖 **Gemini AI** — Generates natural-language responses based on retrieved context.
* 💬 **Multi-Turn Chat** — Maintains previous conversation using Streamlit session state.
* 📖 **Conversation Context** — Uses recent chat history to understand follow-up questions.
* 📑 **Source Citations** — Displays retrieved document pages and snippets through the `View Source` section.
* 📄 **PDF Ingestion** — Extracts text from the knowledge-base PDF using `pypdf`.
* 🖥️ **Streamlit UI** — Provides a simple and interactive chatbot interface.
* 🔐 **Environment Variables** — Gemini API credentials are stored in `.env` rather than hard-coded in the source code.

---

## 🏗️ Project Architecture

```text
User Question
      ↓
Streamlit Chat UI
      ↓
Chat History
      ↓
Question + Conversation Context
      ↓
Sentence Transformer
      ↓
Query Embedding
      ↓
ChromaDB
      ↓
Relevant Document Chunks
      ↓
Gemini API
      ↓
Generated Answer
      ↓
Answer + Source Citation
```

---

## 📁 Project Structure

```text
Chatbot/
│
├── app.py
├── rag.py
├── ingest.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── documents/
│   └── knowledge_base.pdf
│
└── vector_db/
    └── ChromaDB files
```

> `.env` and `vector_db/` should remain local and should not be committed to GitHub.

---

## 🧩 Main Files

### `app.py`

Contains the Streamlit user interface.

It handles:

* Chat input
* Chat messages
* Conversation history
* Assistant responses
* Source display
* `View Source` expander

---

### `rag.py`

Contains the main RAG pipeline.

It handles:

* Loading the embedding model
* Connecting to ChromaDB
* Retrieving relevant document chunks
* Formatting conversation history
* Sending context to Gemini
* Generating the final answer
* Returning source information

---

### `ingest.py`

Processes the knowledge-base PDF.

The ingestion pipeline:

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embeddings
 ↓
ChromaDB
```

The PDF is parsed using `pypdf`, and the resulting document chunks are stored in ChromaDB for later retrieval.

---

### `requirements.txt`

Contains the Python dependencies required to run the project.

Example dependencies include:

```text
streamlit
google-genai
chromadb
sentence-transformers
python-dotenv
pypdf
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Chatbot
```

### 2. Create a Virtual Environment

Using Conda:

```bash
conda create -n rag_chatbot python=3.11
```

Activate it:

```bash
conda activate rag_chatbot
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The application loads the API key using `python-dotenv`.

**Never commit your `.env` file or expose your API key publicly.**

---

## 📄 Add Knowledge Base

Place your PDF inside:

```text
documents/
```

For example:

```text
documents/
└── knowledge_base.pdf
```

---

## 🗃️ Run PDF Ingestion

Before starting the chatbot, run:

```bash
python ingest.py
```

This extracts the PDF text, creates embeddings, and stores the data in ChromaDB.

The local vector database will be created inside:

```text
vector_db/
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The chatbot will open in your browser.

---

## 💬 Multi-Turn Conversation

The chatbot maintains conversation history using:

```python
st.session_state
```

For example:

```text
User:
What is the company's leave policy?

Assistant:
The company provides...

User:
How many days are allowed?

Assistant:
According to the policy...
```

The previous conversation is passed to the RAG pipeline so that follow-up questions can be understood in context.

---

## 📑 Source Verification

Each generated response can display its retrieved source through:

```text
View Source
```

The source section shows:

* Document page number
* Retrieved document snippet

This allows users to verify the information used to generate the answer.

---

## 🖼️ Demo

### Chatbot Interface

Add a screenshot of the running application here:

```text
![RAG Chatbot Interface](screenshots/chatbot.png)
```

### Source Citation

Add a second screenshot here:

```text
![Source Citation](screenshots/source.png)
```

Create a folder in the repository:

```text
screenshots/
```

and place your screenshots inside it.

---

## 🔐 Git Security

The following files/folders should not be committed:

```text
.env
vector_db/
```

Example `.gitignore`:

```text
.env
vector_db/
__pycache__/
*.pyc
```

This prevents API credentials and local ChromaDB files from being tracked by Git.

---

## 🛠️ Technologies Used

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Application development         |
| Streamlit             | Chatbot UI                      |
| Gemini API            | Response generation             |
| Sentence Transformers | Text embeddings                 |
| ChromaDB              | Vector database                 |
| pypdf                 | PDF text extraction             |
| python-dotenv         | Environment variable management |

---

## 🧠 RAG Workflow

The application follows the **Retrieval-Augmented Generation** approach.

### 1. Ingestion

The PDF is loaded and converted into text.

### 2. Chunking

Large text is divided into smaller chunks.

### 3. Embeddings

Each chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

### 4. Storage

The embeddings and document information are stored in ChromaDB.

### 5. Retrieval

When the user asks a question, the question is converted into an embedding and compared with stored vectors.

### 6. Generation

The most relevant chunks are provided to Gemini as context.

### 7. Response

Gemini generates an answer based on the retrieved knowledge-base information.

---
## UI Interface
<img width="995" height="575" alt="Screenshot 2026-09-29 115453" src="https://github.com/user-attachments/assets/1f0e2351-1784-4fb2-9b03-44f34ffc6885" />



<img width="975" height="420" alt="Screenshot 2026-09-29 112834" src="https://github.com/user-attachments/assets/732eedff-9869-4ffd-9007-60771808b463" />

--- 

## ⚠️ API Quota

The project uses the Gemini API. Depending on the selected Gemini API plan, requests may be subject to rate limits or daily quotas.

If the API quota is exceeded, the application may temporarily be unable to generate responses until the quota becomes available again.

---

## 🎯 Project Goal

The goal of this project is to demonstrate a complete end-to-end **RAG-based AI application**, including:

* Document ingestion
* PDF processing
* Text embeddings
* Vector database storage
* Semantic retrieval
* LLM-based answer generation
* Multi-turn conversations
* Source verification
* Interactive Streamlit interface

---

## 👩‍💻 Author

**Laiba Aamer**

BS Artificial Intelligence Student

AI/ML Developer | RAG | Generative AI | Python
