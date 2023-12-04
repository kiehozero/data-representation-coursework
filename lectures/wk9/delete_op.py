"""Lecture material to delete a row."""

import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="test_datarep"
)

cursor = db.cursor()
sql_delete = "DELETE FROM student WHERE id = %s"
values = (2,)

cursor.execute(sql_delete, values)

db.commit()
print("delete done")

db.close()
cursor.close()
