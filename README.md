Company Policy RAG Chatbot
A complete Retrieval-Augmented Generation (RAG) based AI chatbot that allows users to ask questions about company policies and receive answers grounded in the organization's knowledge base.
The system uses document retrieval, semantic embeddings, a vector database, and a Large Language Model (LLM) to provide context-aware answers.

 1. Project Overview
The Company Policy RAG Chatbot is designed to make company-policy information easier to access.
Instead of asking an LLM to answer questions only from its pretrained knowledge, the application retrieves relevant information from company documents and provides that information to the LLM as context.
 Basic Workflow
text
Company Policy Documents
          ↓
     Document Loading
          ↓
        Chunking
          ↓
      Embeddings
          ↓
      ChromaDB
          ↓
      User Question
          ↓
   Query Embedding
          ↓
   Similarity Search
          ↓
 Relevant Document Chunks
          ↓
       Gemini LLM
          ↓
      Final Answer

2. Main Features
* Company-policy question answering
* Retrieval-Augmented Generation
* Semantic document search
* Document chunking
* Sentence Transformer embeddings
* ChromaDB vector database
* Gemini LLM integration
* Streamlit web interface
* Context-grounded responses
* Local company knowledge base
* Environment-variable based API-key management

3. Technologies Used
Technology	Purpose
Python	Main Programming Language
Streamlit	Web-based chatbot interface
ChromaDB	Vector Database
Sentence Transformer	Text Embeddings
All-MiniLM-L6-v2	Embedding Model
Gemini	LLM/ response generation
Python-dotenv	Environment variable management

 4. Project Structure
Chatbot/
│
├── Documents/
│   ├── knowledge_base.pdf
│
├── Vector_db/
│
├── ingest.py
├── rag.py
├── app.py
├── requirements.txt
├── .env

5. Components
Documents/
Contains the company-policy documents used as the chatbot's knowledge base.
ingest.py
Responsible for preparing documents for the RAG system.
The ingestion pipeline performs:
Load Documents
      ↓
Extract Text
      ↓
Split into Chunks
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
This script should be executed whenever the knowledge base is initially created or when documents are updated.
rag.py
Contains the core RAG pipeline.
It performs:
User Query
    ↓
Query Embedding
    ↓
Vector Search
    ↓
Relevant Chunks
    ↓
Context Construction
    ↓
Gemini
    ↓
Final Answer
app.py
Contains the Streamlit user interface.
It allows users to:
1. Enter a company-policy question.
2. Submit the question.
3. Retrieve relevant policy information.
4. Generate an answer using Gemini.
5. Display the response in the browser.

Vector_db/
Stores the vector database generated from the company-policy documents.
The database contains document embeddings and associated information required for semantic retrieval.

6. Installation
Step 1 — Clone or create the project
Place the project in your desired directory.
Example:
cd "C:\Users\Laiba Aamer\Documents\PythonAvin"
Step 2 — Create/activate the environment
If using Anaconda:
powershell
conda activate pytorch_env
Step 3 — Install dependencies
powershell
pip install -r requirements.txt
If `requirements.txt` has not been created yet, the project may require packages such as:
streamlit
chromadb
sentence-transformers
google-genai
python-dotenv

7. Environment Variables
Create a `.env` file in the project root:
GEMINI_API_KEY=your_gemini_api_key
The API key should not be hard-coded directly inside Python files.

8. Creating the Knowledge Base
First, place the company-policy documents inside:
Documents/
Then run:
powershell
python ingest.py
The ingestion script will:
1. Read the documents.
2. Extract their text.
3. Split the text into chunks.
4. Generate embeddings.
5. Store the embeddings in ChromaDB.
After successful ingestion, the vector database will be available in:  Vector_db/
9. Running the Application
Because this project uses Streamlit, the application should be started with:
powershell
streamlit run app.py
Do not normally start the Streamlit application with:
powershell
python app.py
Streamlit will provide a local URL such as:
http://localhost:8501
Open this URL in your browser.

10. How the RAG System Works
Step 1 — User Question
The user enters a question such as:
What is hybrid work means?
Step 2 — Query Embedding
The question is converted into an embedding using:
all-MiniLM-L6-v2
Step 3 — Similarity Search
The query embedding is compared with document embeddings stored in ChromaDB.
Step 4 — Retrieval
The most relevant policy chunks are retrieved.
For example:
Employees may work in hybrid environment 
Combination of approved office and remote locations
Step 5 — Context Creation
The retrieved information is combined into a context.
Step 6 — LLM Generation
The context and user question are sent to Gemini.
Step 7 — Final Response
Gemini generates a response based on the retrieved company-policy information.

11. Example Questions
The chatbot can answer questions such as:
What does hybrid work mean?
What are the company's working hours?
How do I apply for leave?
What is the attendance policy?
What should I do if I am going to be late?
What are the rules for remote work?
What is the company's code of conduct?
How should confidential information be handled?

12. Chunking Strategy
Documents are divided into smaller chunks before embeddings are generated.
A typical configuration can be:
chunk_size = 300
chunk_overlap = 50
Chunking helps the retriever locate specific pieces of information instead of searching through an entire document as one large block.
The exact values can be adjusted depending on document size and retrieval performance.

13. Embedding Model
The project uses:
SentenceTransformer("all-MiniLM-L6-v2")
The embedding model converts text into numerical vectors.
For example:
"Employees can work remotely."
             ↓
       Embedding Model
             ↓
[0.12, -0.34, 0.51, ...]
These vectors are stored in the vector database and used for semantic similarity search.

14. Vector Database
The project uses ChromaDB.
ChromaDB stores:
•	Document chunks
•	Embeddings
•	Document IDs
•	Metadata
When a user asks a question, ChromaDB retrieves the chunks that are most semantically similar to the query.

15. Grounded Responses
The chatbot should answer based on the retrieved company-policy context.
A suitable system instruction is:
Answer the user's question using only the provided company-policy context.

If the answer cannot be found in the provided context,
state that the information is not available in the current
company knowledge base.
Do not invent company policies, dates, working hours,
leave balances, or other policy information.
This helps reduce unsupported answers.

16. Handling Missing Information
If the user asks:
What is the company's travel reimbursement limit?
and the knowledge base does not contain travel reimbursement information, the chatbot should not invent a value.
It should respond with something similar to:
I could not find information about the travel reimbursement
limit in the current company-policy knowledge base.
This behavior is important for a policy-based RAG application.

17. Updating the Knowledge Base
When a company policy changes:
1. Update the relevant document in `Documents/`.
2. Re-run the ingestion process.
3. Verify that the updated information is retrieved.
4. Test questions related to the changed policy.

18. Security Considerations
The project should follow these practices:
•	Never hard-code API keys.
•	Keep `.env` out of GitHub.
•	Do not expose confidential company documents.
•	Restrict access to sensitive information.
•	Do not send confidential data to unauthorized external AI services.
•	Keep production credentials secure.
•	Validate documents before adding them to the knowledge base.

19. Hugging Face Authentication
The embedding model may be downloaded from the Hugging Face Hub.
Without authentication, a warning may appear:
Warning: You are sending unauthenticated requests to the HF Hub.
This is generally a warning rather than an application failure.
A Hugging Face token can be configured when higher rate limits or authenticated Hub access is required.

20. Future Improvements
•	The project can be extended with:
•	PDF document ingestion
•	DOCX document ingestion
•	Multiple document formats
•	Source citations
•	Conversation history
•	Hybrid search
•	Reranking
•	Metadata filtering
•	Authentication
•	Role-based access control
•	Admin document upload
•	Document versioning
•	RAG evaluation
•	Feedback collection
•	Better UI/UX
•	Deployment to a cloud platform

21. Learning Outcomes
This project demonstrates understanding of:
•	Retrieval-Augmented Generation
•	LLM applications
•	Semantic search
•	Text embeddings
•	Vector databases
•	Document chunking
•	Similarity search
•	Context construction
•	Prompt engineering
•	Gemini API integration
•	Streamlit application development
•	Environment-variable management
•	Knowledge-base design

22. Conclusion
The Company Policy RAG Chatbot demonstrates how an LLM can be connected to a private company knowledge base.
Instead of relying exclusively on the model's pretrained knowledge, the application retrieves relevant company-policy information and provides it to the LLM as context.

23. Project Status
Project: Company Policy RAG Chatbot
Architecture: Retrieval-Augmented Generation
Vector Database: ChromaDB
Embedding Model: all-MiniLM-L6-v2
LLM: Gemini
Interface: Streamlit
Status: Development / Testing
