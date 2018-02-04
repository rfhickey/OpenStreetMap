import re
import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

lower = re.compile(r'^([a-z]|_)*$') 
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$') 
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')  

def key_type(element, keys):
    if element.tag == "way":
        for tag in element.iter("tag"):
            k = tag.get("k")
            if lower.search(k):
                keys['lower'] +=1
            elif lower_colon.search(k):
                keys['lower_colon'] +=1
            elif problemchars.search(k):
                keys['problemchars'] +=1
            else:
                keys['other'] +=1
    
    return keys
              
def process_map(SAMPLE_FILE):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for event, element in ET.iterparse(SAMPLE_FILE, events=("start",)):
        keys = key_type(element, keys)
        
    print keys
        
process_map(SAMPLE_FILE)

def test():
    keys = process_map(SAMPLE_FILE)

