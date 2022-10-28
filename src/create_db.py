import mysql.connector
mysql_con = mysql.connector.connect(user='root', password='', host='localhost', database='flask_db')
cursor = mysql_con.cursor()
cursor.execute("show databases")
for db in cursor:
    print(db)
mysql_con.close()