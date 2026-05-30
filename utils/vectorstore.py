import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "vectorstore/faiss_index.bin"
CHUNK_PATH = "vectorstore/chunks.pkl"


def save_vectorstore(embeddings, chunks):

    os.makedirs("vectorstore", exist_ok=True)

    dimension = embeddings.shape[1]

    if os.path.exists(INDEX_PATH):

        index = faiss.read_index(INDEX_PATH)

        with open(CHUNK_PATH, "rb") as f:
            existing_chunks = pickle.load(f)

        index.add(np.array(embeddings))

        existing_chunks.extend(chunks)

        faiss.write_index(index, INDEX_PATH)

        with open(CHUNK_PATH, "wb") as f:
            pickle.dump(existing_chunks, f)

    else:

        index = faiss.IndexFlatL2(dimension)

        index.add(np.array(embeddings))

        faiss.write_index(index, INDEX_PATH)

        with open(CHUNK_PATH, "wb") as f:
            pickle.dump(chunks, f)


def load_vectorstore():

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNK_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks