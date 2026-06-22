import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_10
    (SNO INT PRIMARY KEY NOT NULL,
    Roll_No INT NOT NULL,
    Name TEXT NOT NULL,
    AGE INT DEFAULT (15),
    GENDER TEXT NOT NULL,
    Email_ID TEXT NOT NULL,
    Contact_No REAL NOT NULL)''');

print("Table created successfully")

conn.execute("""INSERT INTO CLASS_10   
(SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) 
             VALUES (1,1,'allen',14,'male','allen@GMAIL.COM',78909809)""");
conn.execute("""INSERT INTO CLASS_10   
(SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No)
              VALUES (2,2,'aish',15,'female','aish@GMAIL.COM',78909909)""");
conn.execute("""INSERT INTO CLASS_10   
(SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) 
             VALUES (3,3,'jake',14,'male','jake@GMAIL.COM',78909009)""");
conn.commit()
print("records created sucsesfully")
import pandas as pd
tables=pd.read_sql("""SELECT *
                   FROM sqlite_master
                   WHERE type='table';""",conn)
tables
class_10d=pd.read_sql("""SELECT *
                   FROM FROM CLASS_10""",conn)
class_10d.head()