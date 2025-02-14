import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),  # Ensure this exists
}
# Create a connection pool
connection_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)

def connect_db():
    """Fetches a connection from the pool and selects the database."""
    try:
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        print(dbconfig['database'])
        cursor.execute(f"USE {dbconfig['database']}")  # Ensure database selection
        cursor.close()
        print("Connected to database!")
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None
  

connect_db()
