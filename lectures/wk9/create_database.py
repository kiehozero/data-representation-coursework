"""Lecture notes on connecting to SQL with Python."""
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()
# Using this method of writing a statement then adding each value later
# getting around potential injection attacks
sql_create = "CREATE DATABASE test_datarep"
cursor.execute(sql_create)

db.close()
cursor.close()
