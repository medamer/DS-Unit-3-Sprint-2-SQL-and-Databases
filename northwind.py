import sqlite3


# connect to the database:
path = "sprintchallange/northwind_small.sqlite3"
connection = sqlite3.connect(path)
print('Connection', connection)

cursor= connection.cursor()
print('Cursor', cursor)

# What are the ten most expensive items 
# (per unit price) in the database:
query = "SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;"
result = cursor.execute(query).fetchall()
print('Ten most expensive items : ', result)

"""
OUTPUT:
Ten most expensive items :  [('Côte de Blaye',), ('Thüringer Rostbratwurst',), 
('Mishi Kobe Niku',), ("Sir Rodney's Marmalade",), ('Carnarvon Tigers',), ('Raclette Courdavault',), 
('Manjimup Dried Apples',), ('Tarte au sucre',), ('Ipoh Coffee',), ('Rössle Sauerkraut',)]
"""

#What is the average age of an employee 
# at the time of their hiring:
query1 = "SELECT AVG (age) From(SELECT (strftime('%Y', HireDate) - strftime('%Y', BirthDate)) - (strftime('%m-%d', HireDate) < strftime('%m-%d', BirthDate)) as age from Employee)"
result1 = cursor.execute(query1).fetchall()
print('Average age :', result1)

"""
OUTPUT:
Average age : [(36.77777777777778,)]
"""

# What are the ten most expensive items (per unit price)
# in the database *and* their suppliers?
query2 = "select ProductName, CompanyName from Product LEFT JOIN Supplier on Product.SupplierId = Supplier.Id order by UnitPrice DESC limit 10;"
result2 = cursor.execute(query2).fetchall()
print("Ten most expensive items and suppliers:", result2)

"""
OUTPUT:
Ten most expensive items and suppliers: [('Côte de Blaye', 'Aux joyeux ecclésiastiques'), 
('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe Niku', 'Tokyo Traders'), 
("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'), ('Carnarvon Tigers', 'Pavlova, Ltd.'), 
('Raclette Courdavault', 'Gai pâturage'), ('Manjimup Dried Apples', "G'day, Mate"), ('Tarte au sucre', "Forêts d'érables"), 
('Ipoh Coffee', 'Leka Trading'), ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]
"""

# What is the largest category
# (by number of unique products in it)?
query3 = "select CategoryName FROM Category WHERE (SELECT count(distinct ProductName) from Product LEFT JOIN Category on Product.CategoryId = Category.Id ORDER BY count(distinct ProductName) DESC) LIMIT 1;"
result3 = cursor.execute(query3).fetchall()
print('The largest category : ', result3)

"""
OUTPUT:
The largest category :  [('Beverages',)]
"""