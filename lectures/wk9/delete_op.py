"""Lecture material to delete a row."""
import pymysql
import config

db = pymysql.connect(
    host="localhost",
    user=config.conkeys["user"],
    password=config.conkeys["pw"],
    database=config.conkeys["db"]
)

cursor = db.cursor()
sql_delete = "DELETE FROM student WHERE id = %s"
values = (2,)

cursor.execute(sql_delete, values)

db.commit()
print("delete done")

db.close()
cursor.close()
