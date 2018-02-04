cur.execute('SELECT COUNT(DISTINCT(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

