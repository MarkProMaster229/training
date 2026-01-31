import psycopg2
from psycopg2.extras import RealDictCursor
import time
import os
from dotenv import load_dotenv
#pip install psycopg2-binary
#pip install fastapi uvicorn asyncpg sqlalchemy alembic python-dotenv
DB_HOST = "127.0.0.1" # Database host
DB_PORT = 5432 # Database port
DB_USER = "postgres" # Database user
DB_PASSWORD = "123456789" # Database password
DB_NAME = "database1" # Database name

class Database:
    def connection1(self):
        self.connection = psycopg2.connect( # Establishing the connection
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )

    def Tables(self, stuff):
            self.connection1()
            cursor = self.connection.cursor()
            cursor.execute("""
                           INSERT INTO MyData1 (stuff) 
                           VALUES (%s)
                           """, (stuff,))
            self.connection.commit()
            cursor.close()

    def importDataInTables(self, stuff):
         #this opening table and inserting data in it
         #I wanna give qustion users - you do give me name stuff??????
        #stuff = input()
        if stuff == "":
            print("str - empty")
        
        self.Tables(stuff)
            