import sqlite3
import csv
from pprint import pprint

sqlite_file = 'SQL_Salt_Lake.db'

conn = sqlite3.connect(sqlite_file)

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS ways_nodes''')
conn.commit()

cur.execute('''CREATE TABLE ways_nodes(id INTEGER NOT NULL, node_id INTEGER NOT NULL, position INTEGER NOT NULL, FOREIGN KEY (id) REFERENCES ways(id), FOREIGN KEY (node_id) REFERENCES nodes (id))''');
conn.commit()

with open('ways_nodes.csv','rb') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'].decode("utf-8"), i['node_id'].decode("utf-8"), i['position'].decode("utf-8")) for i in dr]
    

cur.executemany("INSERT INTO ways_nodes(id, node_id, position) VALUES (?, ?, ?);", to_db)

conn.commit()

# cur.execute('SELECT * FROM ways_nodes');
# all_rows = cur.fetchall()
# print('1):')
# pprint(all_rows)

