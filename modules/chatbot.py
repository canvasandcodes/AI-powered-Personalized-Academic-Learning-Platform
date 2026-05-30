import streamlit as st

from utils.retriever import retrieve_context
from utils.gemini_chat import ask_gemini

from utils.analytics_tracker import (
    increment_metric,
    track_topic,
    add_activity
)


def chatbot_ui():

    st.title("Academic Chatbot")

    st.write(
        "Ask questions directly from your uploaded academic materials."
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input(
        "Ask a Question",
        key="chatbot_question"
    )

    if st.button(
        "Ask",
        use_container_width=True,
        key="chatbot_ask_button"
    ):

        if not question:

            st.warning(
                "Please enter a question."
            )

            return

        try:

            with st.spinner(
                "Searching academic materials..."
            ):

                result = retrieve_context(
                    question
                )

                context = result["context"]

                sources = result.get(
                    "sources",
                    []
                )

                answer = ask_gemini(
                    question,
                    context
                )

                increment_metric(
                    "questions_asked"
                )

                track_topic(
                    question
                )

                add_activity(
                    f"Chatbot Question: {question}"
                )

                st.session_state.chat_history.insert(
                    0,
                    {
                        "question": question,
                        "answer": answer,
                        "sources": sources
                    }
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

    st.divider()

    if st.session_state.chat_history:

        st.subheader(
            "Conversation"
        )

        for idx, chat in enumerate(
            st.session_state.chat_history
        ):

            with st.container(
                border=True
            ):

                st.markdown(
                    f"""
                    ### Question

                    {chat['question']}
                    """
                )

                st.markdown(
                    f"""
                    ### Answer

                    {chat['answer']}
                    """
                )

                if chat["sources"]:

                    with st.expander(
                        "Source References"
                    ):

                        for source in chat[
                            "sources"
                        ]:

                            st.write(
                                source
                            )

    else:

        st.info(
            "No questions asked yet."
        )