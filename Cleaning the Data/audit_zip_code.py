postal_type_re = re.compile('(?<!\d)\d{5}(?!\d)')      # Looks for postal codes that are five digits. Reference: https://stackoverflow.com/questions/3532947/python-regular-expression-match-all-5-digit-numbers-but-none-larger

def audit_postal_code(postal_types, postal_code):     
    m = postal_type_re.search(postal_code) # Looks for postal codes that are # of digits and sets them equal to m.
    if m:                                  # If the postal code (m) is # digits, proceed.      
        postal_type = m.group()            # Take the postal codes that are # digits, groups them, and sets them equal to postal_type.
        postal_types[postal_type].add(postal_code) # Take those postal codes that are # digits and adds them to the postal types dictionary.  
    
               
def audit1(SAMPLE_FILE):
    open(SAMPLE_FILE, "r")
    postal_types = defaultdict(set)
    for event, elem in ET.iterparse(SAMPLE_FILE, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == 'addr:postcode':
                    audit_postal_code(postal_types, tag.attrib['v'])
                    
    return postal_types   

audit1(SAMPLE_FILE)

