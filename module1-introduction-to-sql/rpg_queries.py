import os
import sqlite3


path = "module1-introduction-to-sql/rpg_db.sqlite3"

connection = sqlite3.connect(path)
print('Connection', connection)

cursor = connection.cursor()
print('Cursor', cursor)

# How many total Characters are there?
query = "SELECT count(distinct character_id) as character_count FROM charactercreator_character_inventory;"
result = cursor.execute(query).fetchall()
print('The Total Characters : ', result)

# How many of each specific subclass?


# How many total Items?
query_3 = "SELECT count(distinct name) as total_items FROM armory_item;"
result_3 = cursor.execute(query_3).fetchall()
print('Total Items : ', result_3)

# How many of the Items are weapons? How many are not?
query_4 = "SELECT count(distinct name) as total_weapons FROM armory_weapon JOIN armory_item on item_ptr_id = item_id;"
result_4 = cursor.execute(query_4).fetchall()
print('Total weapons : ', result_4)

result_5 = result_3-result_4
print('Total Not Weapons', result_5)

# How many Items does each character have? (Return first 20 rows)
query_6 = "SELECT item_id, count(item_id) as Total_item FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;"
result_6 = cursor.execute(query_6).fetchall()
print('Total Items per Character (1st 20) : ', result_6)

# How many Weapons does each character have? (Return first 20 rows)
query_7 = "SELECT item_ptr_id, character_id, count(item_ptr_id) as Total_weapons FROM armory_weapon JOIN charactercreator_character_inventory on item_ptr_id = item_id GROUP BY character_id LIMIT 20;"
result_7 = cursor.execute(query_7).fetchall()
print('Total Items per Character (1st 20) : ', result_7)

# On average, how many Items does each Character have?
query_8 = "SELECT AVG(item_count) as avg_item_per_char FROM ( SELECT c.character_id,count(distinct w.item_id) as item_count FROM charactercreator_character c LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id LEFT JOIN armory_item w ON inv.item_id = w.item_id GROUP BY c.character_id) subq;"
result_8 = cursor.execute(query_8).fetchall()
print('The average item per character : ', result_8)

# On average, how many Weapons does each character have?
query_9 = "SELECT AVG(weapon_count) as avg_weapons_per_char FROM ( SELECT c.character_id,count(distinct w.item_ptr_id) as weapon_count FROM charactercreator_character c LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id GROUP BY c.character_id) subq;"
result_9 = cursor.execute(query_9).fetchall()
print('The average weapons per character : ', result_9)
