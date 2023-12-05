"""Lecture material to create a table."""
import pymysql
import configdb

db = pymysql.connect(
    host="localhost",
    user=configdb.conkeys["user"],
    password=configdb.conkeys["pw"],
    database=configdb.conkeys["db"]
)

cursor = db.cursor()
sql_table = """CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250), age INT)"""

cursor.execute(sql_table)

db.close()
cursor.close()
