cur.execute('SELECT COUNT(*) FROM ways');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

