import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234", )

if conn.is_connected():
    print("Connected to MySQL database")
print(conn)
print(conn.is_connected())

