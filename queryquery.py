import pandas as pd 
import sqlite3
conn=sqlite3.connect("database.sqlite")
print("done")
tables=pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in Database:")
print(tables.to_string(index=False), "\n")

print("Team Table:")
team = pd.read_sql("SELECT * FROM Team;", conn)
print(team.head(), "\n")

print("Season Table:")
season = pd.read_sql("SELECT * FROM Season;", conn)
print(season.head(), "\n")

csk_matches = pd.read_sql("""
SELECT Match_Id, Team_2 AS Away_Team, Toss_Winner, Match_Winner
FROM Match
""", conn)
csk_matches = pd.read_sql("""
SELECT Match_Id, Team_2 AS Away_Team, Toss_Winner, Match_Winner
FROM Match
WHERE Team_1 = 3 AND Season_Id = 8;
""", conn)

print("CSK Matches (2015):")
print(csk_matches.to_string(index=False), "\n")

csk_wins = pd.read_sql("""
SELECT Match_Id, Team_1, Team_2, Match_Winner
FROM Match
WHERE Match_Winner = 3 AND Season_Id = 8;
""", conn)

print("CSK Wins (2015):")
print(csk_wins.to_string(index=False), "\n")

match_runs = pd.read_sql("""
SELECT Match_Id, Runs_Scored, Innings_No
FROM Batsman_Scored
WHERE Runs_Scored > 5
AND Match_Id IN (
    SELECT Match_Id
    FROM Match
""", conn)