import google.generativeai as genai
import re
import os
from dotenv import load_dotenv

load_dotenv()

def generate_quiz_from_transcript(transcript: str):
    api_key = os.getenv("GEMINI_API_KEY") 
    client = genai.Client(api_key=api_key)

    neutral_prompt = f"""
    Fasse den folgenden Text neutral und sachlich zusammen.
    Entferne Humor, Ironie, Slang, Beleidigungen und persönliche Aussagen.

    TEXT:
    {transcript}
    """

    neutral_response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=neutral_prompt
    )

    if not neutral_response or not neutral_response.candidates:
        return None

    neutral_text = neutral_response.candidates[0].content.parts[0].text.strip()

    quiz_prompt = f"""
    Erstelle ein Quiz mit genau 10 Fragen basierend auf folgendem neutralen Text.

    GIB AUSSCHLIESSLICH GÜLTIGES JSON AUS.
    KEIN Markdown.
    KEINE Erklärungen.
    KEIN Text vor oder nach dem JSON.
    KEINE Backticks.
    KEINE Kommentare.

    TEXT:
    {neutral_text}

    FORMAT (GENAU SO AUSGEBEN):
    [
      {{
        "question_title": "Frage...",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
      }}
    ]
    """

    quiz_response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=quiz_prompt
    )

    if not quiz_response or not quiz_response.candidates:
        return None

    raw_text = quiz_response.candidates[0].content.parts[0].text.strip()
    raw_text = raw_text.replace("```", "").strip()

    json_match = re.search(r"\[.*\]", raw_text, re.DOTALL)
    if json_match:
        return json_match.group(0).strip()

    return None