from sentence_transformers import SentenceTransformer
from utils.vectorstore import load_vectorstore

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(query, top_k=5):

    index, chunks = load_vectorstore()

    query_embedding = model.encode([query])

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    retrieved_text = []
    sources = set()

    for idx in indices[0]:

        if idx < len(chunks):

            chunk = chunks[idx]

            retrieved_text.append(
                chunk["text"]
            )

            sources.add(
                chunk["source"]
            )

    return {
        "context": "\n\n".join(retrieved_text),
        "sources": list(sources)
    }