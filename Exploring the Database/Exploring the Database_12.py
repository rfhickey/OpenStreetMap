cur.execute('SELECT value, COUNT(*) as num FROM nodes_tags WHERE key="amenity" GROUP BY value ORDER BY num DESC LIMIT 10');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

