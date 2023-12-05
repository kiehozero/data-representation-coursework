"""Lecture material to update a row."""
import pymysql
import configdb

db = pymysql.connect(
    host="localhost",
    user=configdb.conkeys["user"],
    password=configdb.conkeys["pw"],
    database=configdb.conkeys["db"]
)

cursor = db.cursor()
sql_update = "update student set name= %s, age=%s where id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql_update, values)

db.commit()
print("update done")

cursor.close()
db.close()
