import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE crmdb")

print("db successfully created")