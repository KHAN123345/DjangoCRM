import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='MyPassword@786',
)
#Prepare a cursor object
curserObject=database.cursor()

# CREATE DATA BASE
curserObject.execute("CREATE DATABASE elderco")
print("All done")