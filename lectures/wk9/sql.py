"""Lecture notes on connecting to SQL with Python."""
import pymysql
import config

db = pymysql.connect(
    host="localhost",
    user=config.conkeys["user"],
    password=config.conkeys["pw"],
    database=config.conkeys["db"]
)

cursor = db.cursor()
# Using this method of writing a statement then adding each value later
# getting around potential injection attacks
sql_insert = "INSERT INTO student (name, address) VALUES (%s, %s)"
values = ("Mary", "Galway")
cursor.execute(sql_insert, values)
# # You only need to commit a change for Create, Update or Delete commands
db.commit()

# printing query results to the console
sql_read = "SELECT + FROM student WHERE id = %s"
id_val = (1,)
cursor.execute(sql_read, id_val)
# you can also use fetchOne here if you know there will only be one result
result = cursor.fetchall()
for x in result:
    print(x)

cursor.close()
# it's a good idea to close connections because if somebody keeps sending
# requests to your server then it could crash
db.close()

