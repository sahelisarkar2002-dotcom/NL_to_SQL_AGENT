from google import genai
import streamlit as st

# Read Gemini key from Streamlit secrets
api_key = st.secrets["gemini_api_key"]

print("Gemini API key loaded successfully.")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Say Hello in one sentence."
)

print("Gemini response:")
print(response.text)