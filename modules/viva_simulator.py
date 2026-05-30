import streamlit as st

from utils.retriever import retrieve_context
from utils.gemini_chat import ask_gemini

from utils.pdf_generator import generate_pdf

from utils.analytics_tracker import (
    increment_metric,
    track_topic,
    add_activity
)


def viva_simulator_ui():

    st.title("Viva Simulator")

    st.write(
        "Practice viva examinations and receive AI-powered evaluation."
    )

    topic = st.text_input(
        "Topic / Subject",
        key="viva_topic"
    )

    if "viva_question" not in st.session_state:
        st.session_state.viva_question = ""

    if "viva_evaluation" not in st.session_state:
        st.session_state.viva_evaluation = ""

    if st.button(
        "Generate Viva Question",
        use_container_width=True,
        key="generate_viva_question_btn"
    ):

        if not topic:

            st.warning(
                "Please enter a topic."
            )

            return

        try:

            with st.spinner(
                "Generating viva question..."
            ):

                result = retrieve_context(
                    topic
                )

                context = result["context"]

                prompt = f"""
Generate ONE university-level viva question.

RULES:

1. Ask only one question.
2. Make it conceptual.
3. Suitable for oral examination.
4. Use professional academic language.
5. No markdown symbols.

ACADEMIC CONTENT:

{context}
"""

                question = ask_gemini(
                    topic,
                    prompt
                )

                st.session_state.viva_question = question

                increment_metric(
                    "viva_sessions"
                )

                track_topic(
                    topic
                )

                add_activity(
                    f"Started Viva: {topic}"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

    if st.session_state.viva_question:

        st.divider()

        st.subheader(
            "Viva Question"
        )

        with st.container(
            border=True
        ):

            st.write(
                st.session_state.viva_question
            )

        answer = st.text_area(
            "Your Answer",
            height=200,
            key="viva_answer"
        )

        if st.button(
            "Evaluate Answer",
            use_container_width=True,
            key="evaluate_viva_btn"
        ):

            if not answer:

                st.warning(
                    "Please enter your answer."
                )

                return

            try:

                with st.spinner(
                    "Evaluating answer..."
                ):

                    result = retrieve_context(
                        topic
                    )

                    context = result["context"]

                    evaluation_prompt = f"""
You are a university professor.

QUESTION:

{st.session_state.viva_question}

STUDENT ANSWER:

{answer}

REFERENCE CONTENT:

{context}

Evaluate using this structure:

SCORE

Strengths

Weaknesses

Suggested Improvements

Ideal Answer

Use professional academic language.
Do not use markdown symbols.
"""

                    evaluation = ask_gemini(
                        answer,
                        evaluation_prompt
                    )

                    st.session_state.viva_evaluation = evaluation

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

    if st.session_state.viva_evaluation:

        st.divider()

        st.subheader(
            "Evaluation Report"
        )

        with st.container(
            border=True
        ):

            st.text_area(
                "",
                st.session_state.viva_evaluation,
                height=500,
                key="viva_report_output"
            )

        try:

            pdf_path = generate_pdf(
                st.session_state.viva_evaluation,
                "VivaReport",
                "exports/viva",
                topic if topic else "Viva"
            )

            with open(
                pdf_path,
                "rb"
            ) as file:

                st.download_button(
                    label="Download Viva Report PDF",
                    data=file,
                    file_name=pdf_path.split("\\")[-1].split("/")[-1],
                    mime="application/pdf",
                    use_container_width=True,
                    key="download_viva_pdf"
                )

        except Exception as e:

            st.error(
                f"PDF Export Error: {str(e)}"
            )