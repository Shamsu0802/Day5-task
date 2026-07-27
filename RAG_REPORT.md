# Mini RAG Pipeline Report

## Implementation Steps

Initially, I loaded the `kb_documents.json` file and generated embeddings for all 26 knowledge base documents using the **all-MiniLM-L6-v2** Sentence Transformer model.

Next, I stored the generated embeddings in a **FAISS** index and saved the document information separately in a pickle (`documents.pkl`) file. I chose FAISS because the dataset is small and it provides fast similarity search.

After that, I built the retrieval pipeline. Whenever a user enters a query, the query is converted into an embedding using the same embedding model. The FAISS index is then searched to retrieve the **top 3 (k = 3)** most relevant documents. I selected **k = 3** because it provides enough context without retrieving too many unrelated documents.

Then, I created a prompt that instructs the LLM to answer only using the retrieved documents. The retrieved context and the user query are passed to the **Llama 3.1 8B** model through the Groq API to generate the final answer.

While testing the pipeline, I encountered an issue with the `eval_queries.csv` file. Some queries contained commas, which caused parsing errors. Instead of modifying the data directly, I first wrote a small Python script to inspect the CSV line by line and identify the exact issue. After confirming the formatting problem, I corrected the CSV so that all queries could be read successfully.

Finally, I ran the pipeline for all 12 evaluation queries and stored the retrieved document IDs and generated answers in `query_results.json`.

## Handling Insufficient Information

The prompt instructs the model to answer only from the retrieved context. If the retrieved documents do not contain enough information to answer the query, the model responds:

> "I don't have enough information in the TicketOps knowledge base."

This prevents the model from generating unsupported or incorrect answers.

## Retrieval Quality

I manually reviewed the retrieved documents for all 12 queries. Most queries retrieved the correct documents and produced accurate answers. Queries that were not covered by the knowledge base, such as the weather-related query and the prompt injection query, correctly returned that the required information was not available instead of generating misleading answers.