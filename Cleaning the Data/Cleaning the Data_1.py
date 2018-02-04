def update_name(name, mapping):

    m = street_type_re.search(name)
    if m.group() not in expected:
        if m.group() in mapping.keys():
            name = re.sub(m.group(), mapping[m.group()], name)
    return name

def test():
    st_types = audit(SAMPLE_FILE)
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems(): 
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
           
test()

