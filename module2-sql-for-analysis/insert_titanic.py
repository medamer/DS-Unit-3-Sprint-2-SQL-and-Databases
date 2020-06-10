import os
import json
import csv
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() 

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# Create the titanic file to the SQL server:
query = "CREATE TABLE titanic (Survived int, Pclass int, Name varchar, Sex varchar, Age float, Siblings_Spouses_Aboard int, Parents_Children_Aboard int,Fare float);"
cursor.execute(query)
print('Table created')

# Upload the csv file into server:
with open('titanic.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO titanic VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
print('File Uploaded')

connection.commit() # Commit the changes to the server:

# Read from the file:
query2 = "SELECT * FROM titanic WHERE Survived = 1 and Age = 80 ;"
result = cursor.execute(query2)
print(result)

cursor.close()
connection.close()

# python -m module2-sql-for-analysis.insert_titanic