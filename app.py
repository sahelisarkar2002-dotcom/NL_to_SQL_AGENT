import streamlit as st

from nl_to_sql import generate_sql
from database import run_query


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="NL to SQL Agent",
    page_icon="🧠",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🧠 Natural Language to SQL Agent")

st.write(
    "Ask questions about the loan database using natural language. "
    "Gemini will convert your question into SQL and execute it on Aiven MySQL."
)


# -----------------------------
# User Input
# -----------------------------

question = st.text_input(
    "Enter your question:",
    placeholder="Example: Show all female customers"
)


# -----------------------------
# Generate SQL and Execute
# -----------------------------

if st.button("Generate & Run SQL"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        try:

            # Generate SQL
            with st.spinner("Generating SQL..."):

                sql = generate_sql(question)


            # Display generated SQL
            st.subheader("Generated SQL")

            st.code(sql, language="sql")


            # Execute SQL
            with st.spinner("Running query on Aiven MySQL..."):

                columns, rows = run_query(sql)


            # Display results
            st.subheader("Query Results")

            if rows:

                data = [dict(zip(columns, row)) for row in rows]

                st.dataframe(
                    data,
                    use_container_width=True
                )

                st.success(
                    f"Query executed successfully! {len(rows)} row(s) returned."
                )

            else:

                st.info("The query executed successfully, but returned no rows.")


        except Exception as e:

            st.error("Something went wrong.")

            st.exception(e)