import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint


street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) #pulls out last word when tag attribute is "v"


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Circle", "West", "East", "North", "South", "Temple", "Way", "Gateway", "Broadway"]

mapping = { "Rd.": "Road",
            "1300": "",
            "N": "North",
            "319": "",
            "A": ""
            }
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(SAMPLE_FILE):
    open(SAMPLE_FILE, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(SAMPLE_FILE, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    
    return street_types

audit(SAMPLE_FILE)

