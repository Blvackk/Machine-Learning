import mysql.connector

conn = mysql.connector.connect(
    host="localhost",           
    user=" root",
    password="1234", 
    database="pythondb"
)

mycursor = conn.cursor()
mycursor.execute("CREATE TABLE student (name VARCHAR(255), branch VARCHAR(255),id int(11) PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)