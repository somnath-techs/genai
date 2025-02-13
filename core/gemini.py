from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def gemini_text_summerization(text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Summerize this : {text}"
    )
    return response.text