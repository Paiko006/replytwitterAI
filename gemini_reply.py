import google.generativeai as genai
import json

with open("config/credentials.json") as f:
    api_key = json.load(f)["gemini_api_key"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

async def generate_reply(tweet_text: str) -> str:
    prompt = f"Buat balasan yang menarik, relevan, dan sopan untuk tweet ini:\n\n\"{tweet_text}\"\n\nBalasan:"
    response = model.generate_content(prompt)
    return response.text.strip()
