from django.shortcuts import render
from google import genai
from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from the correct location (one level above the Django project)
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def index(request):

    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=question,
            )
            answer = response.text
        except Exception as e:
            answer = f"Error: {e}"

    return render(request, "index.html", {"answer": answer})