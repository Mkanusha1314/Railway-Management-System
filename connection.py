import mysql.connector
from mysql.connector import Error

def create_connection():
    """Establish a database connection to the MySQL database"""
    try:
        # Define connection parameters
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL server host (localhost for local)
            user="root",       # Replace with your MySQL username
            password="Mithun@123",  # Replace with your MySQL password
            database="RailwayDB"  # The database you created for this project
        )

        if conn.is_connected():
            print("Connected to MySQL database")

        return conn

    except Error as e:
        print(f"Error: '{e}'")
        return None

def close_connection(conn):
    """Close the MySQL connection"""
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")

# Usage example
connection = create_connection()

# Now you can execute your SQL queries with this connection
# For example, to fetch all users:
def fetch_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User;")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Fetch and display users
if connection:
    fetch_users(connection)
    close_connection(connection)
