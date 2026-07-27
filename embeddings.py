import json
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base
with open("kb_documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

print(f"Loaded {len(documents)} documents.")

# Extract document contents
doc_texts = [doc["content"] for doc in documents]

# Generate embeddings
print("Generating embeddings...")
embeddings = model.encode(doc_texts, convert_to_numpy=True)

print("Embeddings Shape:", embeddings.shape)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print(f"FAISS index created with {index.ntotal} documents.")

# Save FAISS index
faiss.write_index(index, "faiss_index.index")

# Save document metadata
with open("documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("FAISS index saved successfully.")
print("Document metadata saved successfully.")