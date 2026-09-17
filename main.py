from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


def main():
    project_folder = Path(__file__).parent
    text_file = project_folder / "text.txt"
    chroma_folder = project_folder / "chroma_db"

    if not text_file.exists():
        print(f"Error: {text_file} was not found.")
        return

    with open(text_file, "r", encoding="utf-8") as file:
        textfile = file.read()

    chunks = [
        chunk.strip()
        for chunk in textfile.split("\n\n")
        if chunk.strip()
    ]

    if not chunks:
        print("Error: text.txt does not contain any text chunks.")
        return

    print("CHUNKS:\n")

    for index, chunk in enumerate(chunks):
        print(f"Chunk {index}:")
        print(chunk)
        print()

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Creating ChromaDB client...")
    client = chromadb.PersistentClient(path=str(chroma_folder))

    collection = client.get_or_create_collection(name="documents")

    embeddings = model.encode(chunks).tolist()

    collection.upsert(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    print("Document loaded successfully!")

    question = input("\nEnter your question: ").strip()

    if not question:
        print("No question entered.")
        return

    question_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=min(2, len(chunks))
    )

    print("\nRelevant Information:\n")

    for document in results["documents"][0]:
        print(document)
        print()


if __name__ == "__main__":
    main()