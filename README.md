# Mini RAG Question Answering System

A simple Retrieval-Augmented Generation (RAG) project built with Python, ChromaDB, and Sentence Transformers.

This project reads text from a local file, divides it into smaller chunks, converts those chunks into numerical vector embeddings, stores them in ChromaDB, and retrieves the most relevant chunks for a user's question.

> Note: This project currently performs document retrieval. It does not yet use a large language model to generate a final natural-language answer.

## Project Description

Retrieval-Augmented Generation is a technique used to improve question-answering systems by retrieving relevant information from a knowledge source before generating an answer.

This mini project demonstrates the retrieval part of a RAG pipeline:

1. Read text from `text.txt`.
2. Split the text into paragraphs or chunks.
3. Convert each chunk into an embedding.
4. Store the chunks and embeddings in ChromaDB.
5. Convert the user's question into an embedding.
6. Search ChromaDB for the most similar chunks.
7. Display the retrieved information.

## Features

- Reads content from a local text file.
- Splits text into paragraph-based chunks.
- Generates embeddings with Sentence Transformers.
- Uses the `all-MiniLM-L6-v2` embedding model.
- Stores vectors in a local ChromaDB database.
- Performs semantic similarity search.
- Returns the two most relevant document chunks.
- Uses a persistent ChromaDB directory.
- Runs locally without requiring a separate database server.

## Technologies Used

- Python 3.11
- ChromaDB
- Sentence Transformers
- PyTorch
- NumPy
- Vector embeddings
- Semantic search

## Project Structure

```text
CHUNKS/
│
├── main.py
├── text.txt
├── requirement.txt
├── README.md
├── myenv/
└── chroma_db/
```

### File Description

| File or Folder | Description |
|---|---|
| `main.py` | Main Python program for loading, embedding, storing, and searching documents |
| `text.txt` | Local text document used as the knowledge source |
| `requirement.txt` | List of Python dependencies |
| `README.md` | Project documentation |
| `myenv/` | Local Python virtual environment |
| `chroma_db/` | Persistent ChromaDB storage directory |

> The `myenv/` folder is normally excluded from GitHub using `.gitignore`.

## How the RAG Pipeline Works

```text
text.txt
   │
   ▼
Read document
   │
   ▼
Split into chunks
   │
   ▼
Generate embeddings
   │
   ▼
Store chunks and vectors in ChromaDB
   │
   ▼
User enters a question
   │
   ▼
Generate question embedding
   │
   ▼
Search for similar vectors
   │
   ▼
Display relevant information
```

## Requirements

Make sure the following are installed:

- Python 3.11 or a compatible Python version
- Git
- VS Code, recommended
- Internet connection for downloading the embedding model the first time

## Installation

### 1. Clone the repository

```bash
git clone [https://github.com/YOUR_USERNAME/mini-rag-chromadb.git](https://github.com/YOUR_USERNAME/mini-rag-chromadb.git)
cd mini-rag-chromadb
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv myenv
```

### 3. Activate the virtual environment

```powershell
.\myenv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(myenv)
```

If PowerShell blocks the activation script, run this command once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 4. Install dependencies

If the dependency file is named `requirement.txt`, run:

```powershell
python -m pip install -r requirement.txt
```

If it is named `requirements.txt`, run:

```powershell
python -m pip install -r requirements.txt
```

For computers with limited disk space, use:

```powershell
python -m pip install --no-cache-dir -r requirement.txt
```

## Usage

### 1. Add text to the document

Open `text.txt` and add the information you want the system to search.

Separate different paragraphs with a blank line:

```text
Python is a programming language used for software development and data science.

ChromaDB is a vector database designed to store and search embeddings.

Sentence Transformers can convert text into numerical vector representations.
```

### 2. Run the program

```powershell
python main.py
```

### 3. Enter a question

The program will display the document chunks and ask:

```text
Enter your question:
```

Type a question such as:

```text
What is ChromaDB?
```

The system will display the most relevant chunks from the document.

## Example Output

```text
CHUNKS:

Chunk 0:
Python is a programming language used for software development and data science.

Chunk 1:
ChromaDB is a vector database designed to store and search embeddings.

Loading embedding model...

Creating ChromaDB client...

Document loaded successfully!

Enter your question: What is ChromaDB?

Relevant Information:

ChromaDB is a vector database designed to store and search embeddings.
```

## Main Components

### Text Loading

The program reads the contents of `text.txt`:

```python
with open(text_file, "r", encoding="utf-8") as file:
    textfile = file.read()
```

### Text Chunking

The document is split wherever two newline characters occur:

```python
chunks = [
    chunk.strip()
    for chunk in textfile.split("\n\n")
    if chunk.strip()
]
```

Each paragraph becomes one searchable document chunk.

### Embedding Generation

The Sentence Transformers model converts text into vectors:

```python
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks).tolist()
```

Similar meanings produce vectors that are close to one another in vector space.

### ChromaDB Storage

The chunks and embeddings are stored in a ChromaDB collection:

```python
collection.upsert(
    documents=chunks,
    embeddings=embeddings,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)
```

### Similarity Search

The user's question is also converted into an embedding and searched against the stored vectors:

```python
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=min(2, len(chunks))
)
```

The system returns the two most relevant chunks.

## Important Note About RAG

This version is a retrieval-based RAG prototype.

It includes:

- Document loading.
- Chunking.
- Embedding creation.
- Vector storage.
- Similarity search.
- Relevant-context retrieval.

It does not yet include:

- A large language model.
- Automatic answer generation.
- Chat history.
- PDF or DOCX document loading.
- A web interface.
- A REST API.

A future version can send the retrieved chunks to a language model to generate a direct answer.

## Future Improvements

- Add PDF, DOCX, and website document loading.
- Improve chunking with chunk size and overlap.
- Add metadata such as filename and page number.
- Add a FastAPI backend.
- Create a React frontend.
- Add a large language model for answer generation.
- Add conversation history.
- Add source citations.
- Add document upload support.
- Add authentication.
- Deploy the project using Docker or a cloud platform.
- Add evaluation metrics for retrieval quality.

## Common Commands

Activate the environment:

```powershell
.\myenv\Scripts\Activate.ps1
```

Run the project:

```powershell
python main.py
```

Check installed packages:

```powershell
python -m pip list
```

Deactivate the environment:

```powershell
deactivate
```

## Troubleshooting

### `Activate.ps1` is not recognized

Make sure you are inside the project directory:

```powershell
cd D:\projects\CHUNKS
```

Then run:

```powershell
.\myenv\Scripts\Activate.ps1
```

### `text.txt` was not found

Make sure `text.txt` is in the same directory as `main.py`:

```text
D:\projects\CHUNKS\text.txt
```

### Package import error

Activate the correct environment:

```powershell
.\myenv\Scripts\Activate.ps1
```

Then install the requirements:

```powershell
python -m pip install -r requirement.txt
```

Check which Python is being used:

```powershell
python -c "import sys; print(sys.executable)"
```

The result should contain:

```text
D:\projects\CHUNKS\myenv
```

### Not enough disk space

Clear the pip cache:

```powershell
python -m pip cache purge
```

Then install without a cache:

```powershell
python -m pip install --no-cache-dir -r requirement.txt
```

##Screenshots
<img width="1920" height="1080" alt="Screenshot 2026-09-17 175507" src="https://github.com/user-attachments/assets/744226ae-92eb-47a8-9d45-045074c63f58" />



## License

This project is available for educational and personal use. You may add an MIT License if you want to make the project open source.

## Author
V.Greeshma

Created by `YOUR_NAME`.

GitHub: `https://github.com/YOUR_USERNAME`
