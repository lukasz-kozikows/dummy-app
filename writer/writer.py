import os, random
from datetime import datetime
import mysql.connector
from quotes import QUOTES

def main():
    cnx = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connection_timeout=5,
    )
    try:
        cur = cnx.cursor()
        cur.execute(
            "INSERT INTO quotes (created_at, quote) VALUES (%s, %s)",
            (datetime.now(), random.choice(QUOTES))
        )
        cnx.commit()
    finally:
        cnx.close()

if __name__ == "__main__":
    main()