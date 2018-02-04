import sqlite3
import csv
from pprint import pprint

sqlite_file = 'SQL_Salt_Lake.db'

conn = sqlite3.connect(sqlite_file)

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS ways''')
conn.commit()

cur.execute('''CREATE TABLE ways(id INTEGER PRIMARY KEY NOT NULL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp TEXT)''');
conn.commit()

with open('ways.csv','rb') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'].decode("utf-8"), i['user'].decode("utf-8"), i['uid'].decode("utf-8"), i['version'].decode("utf-8"), i['changeset'].decode("utf-8"), i['timestamp'].decode("utf-8")) for i in dr]
    

cur.executemany("INSERT INTO ways(id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)

conn.commit()

# cur.execute('SELECT * FROM ways')
# all_rows = cur.fetchall()
# print('1):')
# pprint(all_rows)

