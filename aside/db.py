import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
# print(connection)
cursor = connection.cursor()

cursor.execute("SELECT * FROM Checking_Accounts")
myresult = cursor.fetchall()

for x in myresult:
    print(x)
# print(cursor)
cursor.close()
connection.close()