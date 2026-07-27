# Day 5 Task Build a Mini RAG Pipeline

## What this is

`kb_documents.json` is TicketOps' support knowledge base **26 short
documents** covering account security, billing, integrations, API access,
team management, and troubleshooting. `eval_queries.csv` has **12 test
queries**, unlabeled, that you'll run through your finished pipeline.

This is the retrieval component your capstone project will depend on, so build it like a real reusable piece,
not a one off script.

## What to do

### 1. Embed the knowledge base
Generate embeddings for all 26 documents using any embedding model you have
access to (OpenAI, sentence-transformers, Cohere, etc.) and store them
however you like an in-memory list, a local vector store (Chroma, FAISS),
or a simple dict. For 26 documents you don't need a heavyweight vector
database; make a reasonable choice and be ready to explain it.

### 2. Build retrieval
Given a query, embed it and retrieve the top-k most relevant documents
(pick a sensible k you don't need all 26 back every time). Think about
what "relevant" should mean here: is a plain similarity threshold enough,
or do you need any additional logic?

### 3. Generate a grounded answer
Take the retrieved documents and use an LLM to generate an answer to the
query, **grounded only in the retrieved content** the model shouldn't
answer from its own general knowledge about SaaS products in general, and
it shouldn't answer questions the knowledge base doesn't actually cover.

### 4. Handle the cases where retrieval comes up empty or weak
Some of the 12 queries are **not fully covered** by the knowledge base, on
purpose. Your pipeline should recognize when retrieved documents don't
actually answer the question and respond accordingly saying it doesn't
have that information rather than generating a plausible-sounding answer
anyway.

### 5. Measure retrieval quality
For each of the 12 queries, record which documents you retrieved. You won't
have gold labels for this file, so instead: manually read each query and its
retrieved docs, and judge for yourself whether the right documents came
back. Note any queries where you're not confident retrieval worked well.

### 6. Write a short report (`RAG_REPORT.md`)
Cover: how you chose to store/search embeddings and why, your k value and
why, how your pipeline decides when it doesn't have enough information to
answer, and your own assessment of retrieval quality per query including
where you think it might have failed.

### 7. Deliverables
- Your pipeline code
- Your outputs for all 12 queries (retrieved doc IDs + generated answer,
  saved as `query_results.json` or `.csv`)
- `RAG_REPORT.md`
- Incremental commits, not one dump at the end


## What we're looking for

- Whether you understand what embeddings and similarity search are actually
  doing, not just calling a library
- Whether your system stays grounded in retrieved content instead of
  filling gaps with the model's general knowledge
- Whether you can tell the difference between "the knowledge base doesn't
  cover this" and "my retrieval missed something that's actually there"
- Whether your own quality assessment in the report is honest and specific,
  not just "it worked great"

## This afternoon

Live walkthrough: you'll show your retrieval + generation pipeline running
live against a query I give you on the spot including at least one that
tests whether your system stays grounded rather than making something up.
