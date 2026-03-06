from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="what is adi gender? answer in one word",
)

print(response.text)