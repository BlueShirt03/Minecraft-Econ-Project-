import os 
import psycopg2
from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

def get_connection():
    try:
        connection = psycopg2.connect(
        host = DB_HOST,
        database  = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD,
        port = DB_PORT
    )
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    return connection
    

connection = get_connection()

if connection:
    print ("Database connection successful!")
else:
    print ("Database connection failed.")  

print(connection)