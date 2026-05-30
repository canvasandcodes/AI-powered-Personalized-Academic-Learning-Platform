import streamlit as st
import os
import pickle

CHUNK_PATH = "vectorstore/chunks.pkl"
UPLOAD_DIR = "uploads"


def knowledge_base_ui():

    st.header("Knowledge Base Manager")

    uploaded_files = []

    if os.path.exists(UPLOAD_DIR):

        uploaded_files = [
            file
            for file in os.listdir(UPLOAD_DIR)
            if file.endswith(".pdf")
        ]

    total_documents = len(uploaded_files)

    total_chunks = 0

    if os.path.exists(CHUNK_PATH):

        with open(CHUNK_PATH, "rb") as f:

            chunks = pickle.load(f)

            total_chunks = len(chunks)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📄 Documents",
            total_documents
        )

    with col2:
        st.metric(
            "🧩 Chunks",
            total_chunks
        )

    st.divider()

    st.subheader("Uploaded Documents")

    if uploaded_files:

        for file in uploaded_files:

            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(f"📄 {file}")

            with col2:

                if st.button(
                    "Delete",
                    key=file
                ):

                    file_path = os.path.join(
                        UPLOAD_DIR,
                        file
                    )

                    if os.path.exists(file_path):
                        os.remove(file_path)

                    st.success(
                        f"{file} deleted."
                    )

                    st.rerun()

    else:

        st.info(
            "No documents uploaded."
        )

    st.divider()

    st.subheader("Danger Zone")

    if st.button(
        "🗑️ Clear Entire Knowledge Base",
        type="primary"
    ):

        try:

            if os.path.exists(CHUNK_PATH):
                os.remove(CHUNK_PATH)

            if os.path.exists(
                "vectorstore/faiss_index.bin"
            ):
                os.remove(
                    "vectorstore/faiss_index.bin"
                )

            for file in os.listdir(
                UPLOAD_DIR
            ):

                path = os.path.join(
                    UPLOAD_DIR,
                    file
                )

                if os.path.isfile(path):
                    os.remove(path)

            st.success(
                "Knowledge base cleared successfully."
            )

            st.rerun()

        except Exception as e:

            st.error(
                str(e)
            )