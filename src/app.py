import cx_Oracle

connection = cx_Oracle.connect(user="", password="",
                               dsn="")

cursor = connection.cursor()

cursor.execute("SELECT 1 FROM dual")

row = cursor.fetchone()

print(row[0])

connection.close()
