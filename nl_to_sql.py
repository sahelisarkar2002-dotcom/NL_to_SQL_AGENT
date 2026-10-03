import streamlit as st
from google import genai
from schema import DATABASE_SCHEMA

# Load Gemini API key
api_key = st.secrets["gemini_api_key"]

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_sql(question):

    prompt = f"""
You are an expert MySQL SQL generator.

Your task is to convert the user's natural language question
into a valid MySQL SELECT query.

DATABASE SCHEMA:
{DATABASE_SCHEMA}

RULES:
1. Generate only SELECT queries.
2. Do not generate INSERT, UPDATE, DELETE, DROP, ALTER,
   CREATE, or TRUNCATE queries.
3. Use only tables and columns from the provided schema.
4. Do not invent tables or columns.
5. Use the correct JOIN relationships.
6. Generate valid MySQL syntax.
7. Return ONLY the SQL query.
8. Do not use markdown code fences.

USER QUESTION:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    sql = response.text.strip()

    # Remove markdown code fences if Gemini adds them
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()