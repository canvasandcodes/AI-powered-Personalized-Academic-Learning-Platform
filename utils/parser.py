import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()

LLAMA_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")


def parse_pdf(pdf_path):
    """
    Parse PDF using LlamaParse
    """

    try:
        parser = LlamaParse(
            api_key=LLAMA_API_KEY,
            result_type="markdown"
        )

        documents = parser.load_data(pdf_path)

        extracted_text = ""

        for doc in documents:
            extracted_text += doc.text + "\n"

        return extracted_text

    except Exception as e:
        raise Exception(f"Error parsing PDF: {str(e)}")