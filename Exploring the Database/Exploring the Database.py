import sqlite3
import csv
from pprint import pprint

sqlite_file = 'SQL_Salt_Lake.db'

conn = sqlite3.connect(sqlite_file)

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS nodes_tags''')
conn.commit()

cur.execute('''CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT, type TEXT, FOREIGN KEY(id) REFERENCES nodes(id))''');
conn.commit()

with open('nodes_tags.csv','rb') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'].decode("utf-8"), i['key'].decode("utf-8"), i['value'].decode("utf-8"), i['type'].decode("utf-8")) for i in dr]
    

cur.executemany("INSERT INTO nodes_tags(id, key, value,type) VALUES (?, ?, ?, ?);", to_db)

conn.commit()

# cur.execute('SELECT * FROM nodes_tags')
# all_rows = cur.fetchall()
# print('1):')
# pprint(all_rows)

