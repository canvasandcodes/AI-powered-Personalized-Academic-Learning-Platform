import streamlit as st
from utils.analytics_tracker import load_analytics


def dashboard_ui():

    data = load_analytics()

    st.title("Lumora AI")

    st.caption(
        "Personalized Academic Intelligence Platform"
    )

    st.write(
        """
        AI-powered academic assistant for university learning,
        study notes generation, examination preparation,
        viva practice, intelligent document understanding,
        semantic search and academic knowledge retrieval.
        """
    )

    st.divider()

    st.subheader("Platform Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Documents",
            data.get("documents_uploaded", 0)
        )

    with col2:
        st.metric(
            "Questions",
            data.get("questions_asked", 0)
        )

    with col3:
        st.metric(
            "Notes",
            data.get("notes_generated", 0)
        )

    with col4:
        st.metric(
            "Viva Sessions",
            data.get("viva_sessions", 0)
        )

    st.divider()

    st.subheader("Core Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            "Academic Chatbot\n\nAsk questions from uploaded PDFs."
        )

    with c2:
        st.info(
            "Study Notes Generator\n\nGenerate structured notes instantly."
        )

    with c3:
        st.info(
            "Question Paper Generator\n\nGenerate questions and answers."
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.info(
            "Learning Analytics\n\nTrack usage and engagement."
        )

    with c5:
        st.info(
            "Viva Simulator\n\nPractice viva examinations."
        )

    with c6:
        st.info(
            "Knowledge Base\n\nManage indexed documents."
        )

    st.success(
        "Upload academic materials below to start using Lumora AI."
    )