"""Lecture material to update a row."""
import pymysql
import config

db = pymysql.connect(
    host="localhost",
    user=config.conkeys["user"],
    password=config.conkeys["pw"],
    database=config.conkeys["db"]
)

cursor = db.cursor()
sql_update = "update student set name= %s, age=%s where id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql_update, values)

db.commit()
print("update done")

cursor.close()
db.close()
