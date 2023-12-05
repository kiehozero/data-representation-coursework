"""Lecture material to delete a row."""
import pymysql
import configdb

db = pymysql.connect(
    host="localhost",
    user=configdb.conkeys["user"],
    password=configdb.conkeys["pw"],
    database=configdb.conkeys["db"]
)

cursor = db.cursor()
sql_delete = "DELETE FROM student WHERE id = %s"
values = (2,)

cursor.execute(sql_delete, values)

db.commit()
print("delete done")

db.close()
cursor.close()
