import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


if __name__ == "__main__":
    connection = create_connection()

    if connection.is_connected():
        print("Database connected successfully!")

    connection.close()