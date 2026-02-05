import mysql.connector 

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    database='new',
)

mycursor = conn.cursor()

mycursor.execute(
    'CREATE TABLE IF NOT EXISTS newNames (name VARCHAR(255), age INTEGER(10))')

sqlFormula = 'INSERT INTO newNames (name, age) VALUES (%s, %s)'
values = [('Mark', 16),
          ('Zoe', 15),
          ('Mike', 13),
          ('Noah', 14),
          ('johnny', 15)]

conn.commit()
