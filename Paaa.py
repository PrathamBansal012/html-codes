from google.colab import files
file=files.upload()
import sqlite3
database='database.sqlite'
conn=sqlite3.connect(database)
print('opened data sucsesfully')
import pandas as pd
tables=pd.read_sql("""SELECT*
                   FROM sqlite_master
                   WHERE type='table';""",conn)
tables
teams=pd.read_sql("""SELECT*
                   FROM Teams;""",conn)
teams
MI_wins=pd.read_sql("""SELECT*
                   FROM Match
                   WHERE Match_Winner==7;""",conn)
MI_wins
MI_S8_S9=pd.read_sql("""SELECT*
                   FROM Match
                   WHERE Match_Winner==and Season_Id IN(8,9);""",conn)
MI_S8_S9
MI_wins=pd.read_sql("""SELECT*
                   FROM Match
                   WHERE Match_Winner==7;""",conn)
new_teams=pd.read_sql("""SELECT*
                   FROM Team
                   WHERE Team_Name LIKE 'De%';""",conn)
new_teams
min_max_margin=pd.read_sql("""SELECT MIN(Win_Margin),MAX(Win_Margin) FROM Match""",conn)
min_max_margin