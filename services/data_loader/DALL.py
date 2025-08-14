import mysql.connector

class DAL:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def get_data(self):
        self.cursor.execute("SELECT * FROM data")
        return self.cursor.fetchall()
