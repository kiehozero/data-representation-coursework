"""Lecture material on INSERT operation."""
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="test_datarep"
)

cursor = db.cursor()
sql_insert = "INSERT INTO student (name, age) VALUES (%s,%s)"
values = ("Mary", 21)

cursor.execute(sql_insert, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()
