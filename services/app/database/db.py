import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT")
        )
        return conn
    except Exception as e:
        print("DB Connection Error:", e)
        return None

