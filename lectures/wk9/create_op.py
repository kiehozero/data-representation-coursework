"""Lecture material to create a table."""
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="test_datarep"
)

cursor = db.cursor()
sql_table = """CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250), age INT)"""

cursor.execute(sql_table)

db.close()
cursor.close()
