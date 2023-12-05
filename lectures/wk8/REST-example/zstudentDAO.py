"""Using a class to create re-usable functions. Note that
the cursor and DB are closed after each operation"""
import pymysql
import config


class StudentDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        # these should be read from a config file
        self.host = "localhost"
        self.user = config.conkeys["user"]
        self.password = config.conkeys["pw"]
        self.database = config.conkeys["db"]

    def getCursor(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql = "INSERT INTO student (name, age) VALUES (%s,%s);"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * FROM student;"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "SELECT * FROM student WHERE id = %s;"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    def update(self, values):
        cursor = self.getCursor()
        sql = "UPDATE student SET name= %s, age=%s WHERE id = %s;"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "DELETE FROM student WHERE id = %s;"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        # print("delete done")


studentDAO = StudentDAO()
