cur.execute('SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags WHERE nodes_tags.key="name" GROUP BY nodes_tags.value ORDER BY num DESC LIMIT 5');
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

