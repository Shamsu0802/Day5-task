import json
import pandas as pd

from retriever import retrieve_documents
from generator import generate_answer

# Load evaluation queries
queries = pd.read_csv("eval_queries.csv")

results = []

for _, row in queries.iterrows():

    query_id = row["query_id"]
    question = row["query_text"]

    print(f"\nProcessing {query_id}: {question}")

    # Retrieve documents
    retrieved_docs = retrieve_documents(question)

    # Generate answer
    answer = generate_answer(question, retrieved_docs)

    # Store results
    results.append({
        "query_id": query_id,
        "query": question,
        "retrieved_doc_ids": [doc["doc_id"] for doc in retrieved_docs],
        "answer": answer
    })

# Save results
with open("query_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print("\n✅ All queries processed successfully!")
print("✅ Results saved to query_results.json")