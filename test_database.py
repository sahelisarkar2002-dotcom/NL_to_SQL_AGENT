from database import run_query


sql = """
SELECT *
FROM customers
LIMIT 5;
"""


try:

    columns, rows = run_query(sql)

    print("Query executed successfully!")
    print()

    print("Columns:")
    print(columns)

    print()

    print("Results:")

    for row in rows:
        print(row)

except Exception as e:

    print("Query failed!")
    print(e)