from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_chunks(text, source_name, chunk_size=500, overlap=100):

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk_text = text[start:end]

        chunks.append({
            "text": chunk_text,
            "source": source_name
        })

        start += chunk_size - overlap

    return chunks


def create_embeddings(chunks):

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)

    return embeddings