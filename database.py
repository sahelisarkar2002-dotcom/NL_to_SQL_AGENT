import pymysql
import streamlit as st


def get_connection():

    connection = pymysql.connect(
        host=st.secrets["AIVEN_HOST"],
        port=int(st.secrets["AIVEN_PORT"]),
        user=st.secrets["AIVEN_USERNAME"],
        password=st.secrets["AIVEN_PASSWORD"],
        database=st.secrets["AIVEN_DATABASE"],
        charset="utf8mb4",
        connect_timeout=30
    )

    return connection


def run_query(sql):

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