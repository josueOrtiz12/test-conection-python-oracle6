import cx_Oracle

connection = cx_Oracle.connect("user", "password", "localhost:1521/sid")

cursor = connection.cursor()

cursor.execute("SELECT 1 FROM dual")

row = cursor.fetchone()

print(row[0])

connection.close()
