import mysql.connector
import os


class DBConnection:
    @staticmethod
    def getConnection():
        database = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.environ["MYSQL_PASSWORD"],
            database=os.getenv("MYSQL_DATABASE", "iris"),
        )
        return database


if __name__ == "__main__":
    print(DBConnection.getConnection())