import mysql.connector

conn= mysql.connector.connect(
    host="localhost",       
    user="root",
    password="1234", )

if conn.is_connected():
    print("Connected to MySQL database")

mycursor = conn.cursor()    
mycursor.execute("Create database pythondb")
print(mycursor)
