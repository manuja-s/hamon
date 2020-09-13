import sqlite3
import pandas
con = sqlite3.connect('csv.sqlite')
df = pandas.read_csv('nba.csv')
df.to_sql('nba',con,if_exists='append', index=False)

con.close()

