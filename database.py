import pymysql
import streamlit as st


def get_connection():
    """
    Create and return a connection to Aiven MySQL.
    """

    connection = pymysql.connect(
        host=st.secrets["database"]["host"],
        port=int(st.secrets["database"]["port"]),
        user=st.secrets["database"]["username"],
        password=st.secrets["database"]["password"],
        database=st.secrets["database"]["database"],
        charset="utf8mb4",
        connect_timeout=30
    )

    return connection


def run_query(sql):
    """
    Execute a SELECT query and return
    column names and query results.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        columns = [description[0] for description in cursor.description]

        return columns, rows

    finally:

        cursor.close()
        connection.close()