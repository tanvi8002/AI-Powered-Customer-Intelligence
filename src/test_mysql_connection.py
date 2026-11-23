import pymysql
from getpass import getpass

connection = pymysql.connect(
    host="127.0.0.1",
    user="ai_project",
    password=getpass("Enter your MySQL password: "),
    database="ai_customer_intelligence",
    port=3306
)

print("Successfully connected to MySQL!")

cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
print("MySQL Version:", cursor.fetchone()[0])

cursor.close()
connection.close()