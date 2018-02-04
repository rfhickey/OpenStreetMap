cur.execute('SELECT COUNT(*) FROM nodes');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

