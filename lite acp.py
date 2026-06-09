import sqlite3
conn = sqlite3.connect("database.sqlite")
conn.execute("""
             CREATE TABLE Students(
             ID INTEGER PRIMARY KEY,
             Name TEXT,
             Age INTEGER);
             """)
conn.execute("INSERT INTO STUDENTS(Name,Age)VALUES('ali',15)")
conn.execute("INSERT INTO STUDENTS(Name,Age)VALUES('arah',114)")
conn.commit()
conn.close()
print("database created")