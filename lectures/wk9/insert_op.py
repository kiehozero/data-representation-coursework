"""Lecture material to insert a row."""
import pymysql
import config

db = pymysql.connect(
    host="localhost",
    user=config.conkeys["user"],
    password=config.conkeys["pw"],
    database=config.conkeys["db"]
)

cursor = db.cursor()
sql_insert = "INSERT INTO student (name, age, course) VALUES (%s,%s,%s)"
values = ("Mary", 21, "Anthropology")

cursor.execute(sql_insert, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()
