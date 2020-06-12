import sqlite3

# connect to the database
path = "sprintchallange/demo_data.sqlite3"
connection = sqlite3.connect(path)
print('Connection', connection)

cursor= connection.cursor()
print('Cursor', cursor)

# # create a table:
# query = "CREATE TABLE demo(s varchar, x int, y int);"
# result = cursor.execute(query).fetchall()
# print('Table Created')

# # insert the data:
# query1 = "INSERT INTO demo(s, x, y) VALUES('g', 3, 9), ('v', 5, 7), ('f', 8, 7);"
# result1 = cursor.execute(query1).fetchall()
# print('data added')

# # commit to save the change:
# connection.commit()

# Count how many rows you have:
query2 = "SELECT COUNT(*) FROM demo;"
result2 = cursor.execute(query2).fetchall()
print('Total rows : ', result2)

"""
OUTPUT:
Total rows :  [(3,)]
"""

# How many rows are there where both `x` and `y` are at least 5?
query3 = "SELECT COUNT(*) FROM demo WHERE x >= 5 and y >= 5;"
result3 = cursor.execute(query3).fetchall()
print('Total rows where x and y are at least 5: ', result3)

"""
OUTPUT:
Total rows where x and y are at least 5:  [(2,)]
"""

# How many unique values of `y` are there:
query4 = "SELECT COUNT(DISTINCT y) FROM demo;"
result4 = cursor.execute(query4).fetchall()
print('Unique values in "y" : ', result4)

"""
OUTPUT:
Unique values in "y" :  [(2,)]
"""