# DALL.py
import mysql.connector
import os

class DAL:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "mysql-service")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("MYSQL_ROOT_PASSWORD", "your_password_here")
        self.database = os.getenv("DB_NAME", "your_database_name")

    def get_data(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM data")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

