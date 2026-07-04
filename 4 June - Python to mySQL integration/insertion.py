import mysql.connector

conn = mysql.connector.connect(
    host="localhost",   
    user="root",
    password="1234",    
    database="pythondb"
)

mycursor = conn.cursor()

sql = "INSERT INTO student (name, branch, id) VALUES (%s, %s, %s)"
val = ("John", "IT", 1)

#if user wan to create multiple values then we can use list of tuples
val = [
   ("Alice", "CS", 2),
    ("Bob", "ME", 3)
]

#mycursor.executemany(sql, val)
mycursor.executemany(sql, val)
conn.commit()
print(mycursor.rowcount, "record inserted.")

