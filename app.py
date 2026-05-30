import streamlit as st
import os

from utils.parser import parse_pdf
from utils.embeddings import (
    create_chunks,
    create_embeddings
)

from utils.vectorstore import (
    save_vectorstore
)

from utils.analytics_tracker import (
    increment_metric,
    add_activity
)

from modules.dashboard import dashboard_ui
from modules.chatbot import chatbot_ui
from modules.notes_generator import notes_generator_ui
from modules.exam_generator import exam_generator_ui
from modules.analytics import analytics_ui
from modules.viva_simulator import viva_simulator_ui
from modules.knowledge_base import knowledge_base_ui


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Lumora AI",
    page_icon="L",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# LOAD CSS
# ==================================================

def load_css():

    if os.path.exists("styles.css"):

        with open(
            "styles.css",
            encoding="utf-8"
        ) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


load_css()


# ==================================================
# CREATE FOLDERS
# ==================================================

folders = [
    "uploads",
    "vectorstore",
    "exports",
    "exports/notes",
    "exports/exams",
    "exports/viva",
    "data"
]

for folder in folders:
    os.makedirs(
        folder,
        exist_ok=True
    )


# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
# Lumora AI
Personalized Academic Intelligence Platform
"""
)

st.markdown("---")


# ==================================================
# NAVIGATION
# ==================================================

page = st.radio(
    "",
    [
        "Dashboard",
        "Academic Chat",
        "Study Notes",
        "Question Papers",
        "Analytics",
        "Viva",
        "Knowledge Base"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    dashboard_ui()

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader(
        "Upload Academic Materials"
    )

    uploaded_file = st.file_uploader(
        "",
        type=["pdf"],
        key="main_upload"
    )

    if uploaded_file:

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        if st.button(
            "Process Document",
            use_container_width=True
        ):

            try:

                with st.spinner(
                    "Processing document..."
                ):

                    text = parse_pdf(
                        file_path
                    )

                    chunks = create_chunks(
                        text,
                        uploaded_file.name
                    )

                    embeddings = create_embeddings(
                        chunks
                    )

                    save_vectorstore(
                        embeddings,
                        chunks
                    )

                    increment_metric(
                        "documents_uploaded"
                    )

                    add_activity(
                        f"Uploaded {uploaded_file.name}"
                    )

                st.success(
                    "Document processed successfully."
                )

            except Exception as e:

                st.error(
                    str(e)
                )


# ==================================================
# CHAT
# ==================================================

elif page == "Academic Chat":

    chatbot_ui()


# ==================================================
# NOTES
# ==================================================

elif page == "Study Notes":

    notes_generator_ui()


# ==================================================
# QUESTIONS
# ==================================================

elif page == "Question Papers":

    exam_generator_ui()


# ==================================================
# ANALYTICS
# ==================================================

elif page == "Analytics":

    analytics_ui()


# ==================================================
# VIVA
# ==================================================

elif page == "Viva":

    viva_simulator_ui()


# ==================================================
# KNOWLEDGE BASE
# ==================================================

elif page == "Knowledge Base":

    knowledge_base_ui()


# ==================================================
# FOOTER
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
---
<center>

Lumora AI

Personalized Academic Intelligence Platform

</center>
""",
    unsafe_allow_html=True
)