cur.execute('SELECT user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) GROUP BY user ORDER BY num DESC LIMIT 20');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

