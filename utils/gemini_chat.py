import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(user_input, context):

    prompt = f"""
You are Lumora AI.

Generate professional academic content.

Rules:

- No markdown
- No ###
- No **
- No bullet spam
- Proper headings
- Proper spacing
- Professional formatting

CONTENT:

{context}

REQUEST:

{user_input}
"""

    response = model.generate_content(
        prompt
    )

    return response.text