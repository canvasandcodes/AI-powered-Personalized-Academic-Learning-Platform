import streamlit as st

from utils.retriever import retrieve_context
from utils.gemini_chat import ask_gemini

from utils.pdf_generator import generate_pdf

from utils.analytics_tracker import (
    increment_metric,
    track_topic,
    add_activity
)


def exam_generator_ui():

    st.title("Question Paper Generator")

    st.markdown(
        """
        Generate university-level question papers
        directly from uploaded academic materials.
        """
    )

    topic = st.text_input(
        "Topic / Unit / Chapter"
    )

    question_type = st.selectbox(
        "Question Type",
        [
            "2 Mark Questions",
            "5 Mark Questions",
            "10 Mark Questions",
            "MCQs",
            "Viva Questions"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        min_value=5,
        max_value=20,
        value=10
    )

    if st.button(
        "Generate Question Paper",
        use_container_width=True
    ):

        if not topic:

            st.warning(
                "Please enter a topic."
            )

            return

        try:

            with st.spinner(
                "Generating question paper..."
            ):

                result = retrieve_context(
                    topic
                )

                context = result["context"]

                prompt = f"""
Generate a professional university question paper.

Question Type:
{question_type}

Number of Questions:
{num_questions}

STRICT RULES:

1. No Markdown.
2. No ###.
3. No **.
4. No bullet spam.
5. Include answers after every question.
6. Use professional academic formatting.

FORMAT:

SECTION A

QUESTION 1

Question Text

ANSWER

Answer Text

QUESTION 2

Question Text

ANSWER

Answer Text

Continue until all questions are completed.

CONTENT:
{context}
"""

                questions = ask_gemini(
                    topic,
                    prompt
                )

                increment_metric(
                    "exam_generations"
                )

                track_topic(topic)

                add_activity(
                    f"Generated Question Paper: {topic}"
                )

            st.divider()

            st.subheader(
                "Generated Question Paper"
            )

            with st.container(
                border=True
            ):

                st.text_area(
                    "",
                    questions,
                    height=700
                )

            st.divider()

            pdf_path = generate_pdf(
                questions,
                "QuestionPaper",
                "exports/exams",
                topic
            )

            with open(
                pdf_path,
                "rb"
            ) as file:

                st.download_button(
                    label="Download Question Paper PDF",
                    data=file,
                    file_name=pdf_path.split("\\")[-1].split("/")[-1],
                    mime="application/pdf",
                    use_container_width=True
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )