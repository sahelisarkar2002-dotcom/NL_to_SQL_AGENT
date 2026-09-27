from nl_to_sql import generate_sql
from database import run_query


# Natural language question
question = "Show all female customers"


try:

    # Step 1: Generate SQL using Gemini
    sql = generate_sql(question)

    print("Natural Language Question:")
    print(question)

    print("\nGenerated SQL:")
    print(sql)

    # Step 2: Execute generated SQL on Aiven MySQL
    columns, rows = run_query(sql)

    print("\nQuery executed successfully!")

    print("\nColumns:")
    print(columns)

    print("\nResults:")

    for row in rows:
        print(row)

except Exception as e:

    print("\nError:")
    print(e)