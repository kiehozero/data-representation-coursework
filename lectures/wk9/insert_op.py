"""Lecture material to insert a row."""
import pymysql
import configdb

db = pymysql.connect(
    host="localhost",
    user="root",
    password=configdb.conkeys["pw"],
    database=configdb.conkeys["db"]
)

cursor = db.cursor()
sql_insert = "INSERT INTO student (name, age, course) VALUES (%s,%s,%s)"
values = ("Mary", 21, "Anthropology")

cursor.execute(sql_insert, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()
