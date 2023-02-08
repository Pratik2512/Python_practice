import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()
query = "SELECT * from guvi"
result = cursor.execute(query)

print(cursor.fetchall())

