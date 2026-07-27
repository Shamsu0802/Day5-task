# RAG Report

## Embedding Storage and Search

I generated embeddings for all 26 knowledge base documents using the **all-MiniLM-L6-v2** Sentence Transformers model. I chose this model because it is lightweight, fast, and suitable for semantic search.

I stored the embeddings in a **FAISS** index. Since the knowledge base contains only 26 documents, FAISS was a simple and efficient choice. It performs fast similarity search without requiring a separate vector database. The document metadata was stored in a `documents.pkl` file so that the retrieved indices could be mapped back to the original documents.

---

## K Value

I used **k = 3** for document retrieval. Retrieving the top three documents provided enough context for the LLM to answer most questions while avoiding too many unrelated documents.

---

## Handling Insufficient Information

The retrieved documents are passed to the LLM along with a prompt that instructs it to answer only using the provided context. If the retrieved documents do not contain enough information to answer the question, the model responds:

> "I don't have enough information in the TicketOps knowledge base."

This prevents the model from generating answers that are not supported by the knowledge base.

---

## Retrieval Quality Assessment

I manually reviewed the retrieved documents and generated answers for all 12 evaluation queries.

- **Q01** – Retrieved relevant documents and generated the correct answer, although D01 would ideally rank before D24.
- **Q02** – Retrieved the correct documents and generated the correct answer.
- **Q03** – Retrieved the appropriate security-related documents.
- **Q04** – The knowledge base does not contain Microsoft Teams integration, so the pipeline correctly responded that the information was unavailable.
- **Q05** – Retrieved the correct billing-related documents.
- **Q06** – Retrieved the correct document about account cancellation and data retention.
- **Q07** – Retrieved the correct account recovery document.
- **Q08** – Correctly ignored the prompt injection attempt and answered only based on the knowledge base.
- **Q09** – Retrieved the correct API rate limit information.
- **Q10** – Retrieved the correct refund policy documents.
- **Q11** – Retrieved the correct documents related to CSV export and scheduled automation.
- **Q12** – Since the query was unrelated to the knowledge base, the pipeline correctly responded that it did not have enough information.

Overall, the retrieval worked well for most queries. One area for improvement would be improving the ranking of retrieved documents so that the most relevant document is consistently returned first.
