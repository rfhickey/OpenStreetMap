import re
import xml.etree.cElementTree as ET
import pprint

lower = re.compile(r'^([a-z]|_)*$') # for tags that contain only lowercase letters and are valid
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$') # for otherwise valid tags with a colon in their names
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]') # for tags with problematic characters 

def key_type(element, keys):
    if element.tag == "tag":
        k = element.get("k")
        if re.search(lower,k):
            keys['lower'] +=1
        elif re.search(lower_colon,k):
            keys['lower_colon'] +=1
        elif re.search(problemchars,k):
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
