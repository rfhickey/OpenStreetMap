import sqlite3
import csv
from pprint import pprint

sqlite_file = 'SQL_Salt_Lake.db'

conn = sqlite3.connect(sqlite_file)

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS nodes''')
conn.commit()

cur.execute('''CREATE TABLE nodes(id INTEGER PRIMARY KEY NOT NULL, lat REAL, lon REAL, user TEXT, uid INTEGER, version INTEGER, changeset INTEGER, timestamp TEXT)''');
conn.commit()

with open('nodes.csv','rb') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'].decode("utf-8"), i['lat'].decode("utf-8"), i['lon'].decode("utf-8"), i['user'].decode("utf-8"), i['uid'].decode("utf-8"), i['version'].decode("utf-8"), i['changeset'].decode("utf-8"), i['timestamp'].decode("utf-8")) for i in dr]
    

cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)

conn.commit()

# cur.execute('SELECT * FROM nodes')
# all_rows = cur.fetchall()
# print('1):')
# pprint(all_rows)

