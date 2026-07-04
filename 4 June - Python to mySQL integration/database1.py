import mysql.connector

conn = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="1234",
)

mycursor = conn.cursor()

mycursor.execute("Show databases")

for x in mycursor:
    print(x) 