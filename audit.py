def audit(SAMPLE_FILE):
    open(SAMPLE_FILE, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(SAMPLE_FILE, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    
    return street_types