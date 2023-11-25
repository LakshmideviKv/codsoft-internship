from flask import flask
import sqlite3
conn=sqlite3.connect('test.db')
print ("opened database successfully");
conn.execute('''CREATE TABLE USER
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT     NOT NULL,
            AGE            INT      NOT NULL,
            ADDRESS         CHAR(50),
            SALARY          REAL);''')
conn.execute("INSERT INTO USER(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(1,'LAKSH',19,'PONDY',20000)");
cursor=conn.execute("SELECT id,name,address,salary from USER")

conn.commit()

print("table created successfully")
conn.close()
