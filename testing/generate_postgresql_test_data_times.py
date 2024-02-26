import psycopg2
from psycopg2 import sql
from faker import Faker
import random
from datetime import timedelta

# Replace these with your actual database connection details
db_connection_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'leaderboard_api',
    'user': 'postgres',
    'password': 'password'
}

fake = Faker()

# Generate 100 unique names, times, and milliseconds
data = [(fake.name(), timedelta(
    minutes=random.randint(1, 120),
    seconds=random.randint(1, 59),
    milliseconds=random.randint(1, 999)
)) for _ in range(100)]

# Insert generated data into the table
insert_data_query = sql.SQL("""
    INSERT INTO times (name, stopwatch_time) VALUES (%s, %s)
""")

def insert_data():
    connection = None
    cursor = None
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_connection_params)
        cursor = connection.cursor()

        # Insert generated data into the table
        cursor.executemany(insert_data_query, data)

        # Commit the changes
        connection.commit()

        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_data()