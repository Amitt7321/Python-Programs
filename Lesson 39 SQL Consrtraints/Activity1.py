import sqlite3
import pandas as pd

conn=sqlite3.connect('cities.db')

conn.execute('DROP TABLE IF EXISTS City;')

conn.execute("""
CREATE TABLE City(
City_Id      INTEGER             PRIMARY KEY,
City_Name    TEXT                NOT NULL UNIQUE,
Country      TEXT,
Population   INTEGER,              
Is_Capital   TEXT               DEFAULT 'No'
);
""")
conn.commit()
print('Table created succesfully!')

conn.execute("INSERT INTO City VALUES (1, 'Tokyo', 'Japan', '173000380','Yes');")
conn.execute("INSERT INTO City VALUES (2, 'Nairobi', 'Kenya', '458500380','No');")
conn.execute("INSERT INTO City VALUES (3, 'Mumbai', 'India', '4787770029','Yes');")

conn.commit()
print('Rows inserted successfully!')

cities=pd.read_sql("SELECT* FROM City;",conn)
print(cities)

print("\n---Testing PRIMARY KET---")
try:
   conn.execute("INSERT INTO City VALUES (1, 'Tokyo', 'Japan', '173000380','Yes')'")
   conn.commit()
except Exception as e:
   conn.rollback()
   print("Rejected:",e)
   print("City_ID 1 alredy belongs Tokyo - Primary Key must be unique.")