cur.execute('SELECT tags.value, COUNT(*) as xyz FROM (SELECT * FROM nodes_tags UNION ALL SELECT * FROM ways_tags) tags WHERE tags.key="postcode" GROUP BY tags.value ORDER BY xyz DESC LIMIT 10');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

