"""Lecture material to read a row."""
import pymysql
import configdb

db = pymysql.connect(
    host="localhost",
    user=configdb.conkeys["user"],
    password=configdb.conkeys["pw"],
    database=configdb.conkeys["db"]
)

cursor = db.cursor()
sql_select = "SELECT * FROM student WHERE id = %s"
values = (1,)

cursor.execute(sql_select, values)
result = cursor.fetchall()
for x in result:
    print(x)

db.close()
cursor.close()
