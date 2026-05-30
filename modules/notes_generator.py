import streamlit as st

from utils.retriever import retrieve_context
from utils.gemini_chat import ask_gemini

from utils.pdf_generator import generate_pdf

from utils.analytics_tracker import (
    increment_metric,
    track_topic,
    add_activity
)


def notes_generator_ui():

    st.title("Study Notes Generator")

    st.write(
        "Generate structured university-level study notes from uploaded academic materials."
    )

    topic = st.text_input(
        "Topic / Unit / Chapter",
        key="notes_topic"
    )

    if st.button(
        "Generate Notes",
        use_container_width=True,
        key="generate_notes_btn"
    ):

        if not topic:

            st.warning(
                "Please enter a topic."
            )

            return

        try:

            with st.spinner(
                "Generating study notes..."
            ):

                result = retrieve_context(
                    topic
                )

                context = result["context"]

                prompt = f"""
Generate professional university study notes.

TOPIC:
{topic}

RULES:

1. Use clear headings.
2. Use numbered sections.
3. Include definitions.
4. Include key concepts.
5. Include examples when relevant.
6. Include summary points.
7. Do not use markdown symbols.
8. Use professional academic formatting.

ACADEMIC CONTENT:

{context}
"""

                notes = ask_gemini(
                    topic,
                    prompt
                )

                st.session_state["generated_notes"] = notes

                increment_metric(
                    "notes_generated"
                )

                track_topic(
                    topic
                )

                add_activity(
                    f"Generated Notes: {topic}"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

    if "generated_notes" in st.session_state:

        st.divider()

        st.subheader(
            "Generated Notes"
        )

        with st.container(
            border=True
        ):

            st.text_area(
                "",
                st.session_state["generated_notes"],
                height=600,
                key="notes_output"
            )

        st.divider()

        try:

            pdf_path = generate_pdf(
                st.session_state["generated_notes"],
                "StudyNotes",
                "exports/notes",
                topic if topic else "Notes"
            )

            with open(
                pdf_path,
                "rb"
            ) as file:

                st.download_button(
                    label="Download Notes PDF",
                    data=file,
                    file_name=pdf_path.split("\\")[-1].split("/")[-1],
                    mime="application/pdf",
                    use_container_width=True,
                    key="download_notes_pdf"
                )

        except Exception as e:

            st.error(
                f"PDF Export Error: {str(e)}"
            )