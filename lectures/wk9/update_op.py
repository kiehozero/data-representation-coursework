"""Lecture material to update a row."""
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="test_datarep"
)

cursor = db.cursor()
sql_update = "update student set name= %s, age=%s  where id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql_update, values)

db.commit()
print("update done")

cursor.close()
db.close()
