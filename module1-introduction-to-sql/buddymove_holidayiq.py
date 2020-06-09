import pandas as pd
import sqlite3


path = "module1-introduction-to-sql/buddymove_holidayiq.sqlite3"
connection = sqlite3.connect(path)
print('Connection', connection)

cursor= connection.cursor()
print('Cursor', cursor)

df = pd.read_csv(r'module1-introduction-to-sql/buddymove_holidayiq.csv')
df.to_sql('Review', con=connection)
result = cursor.execute("SELECT * FROM Review").fetchall()

# Get total rows of the table:
query1 = "SELECT count(*) FROM Review;"
result1 = cursor.execute(query1).fetchall()
print('Total Rows : ', result1)

# Get number of users who reviewed 100 Nature and shopping:
query2 = "SELECT count(*) FROM Review WHERE Nature >= 100 and Shopping >= 100;"
result2 = cursor.execute(query2).fetchall()
print('Total Rows : ', result2)