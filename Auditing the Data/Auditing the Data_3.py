def get_user(element):
    if element.tag == "way":
       user = element.get("uid")

       return user
    
def process_map(SAMPLE_FILE):
    users = set()
    for event, element in ET.iterparse(SAMPLE_FILE):
        if get_user(element):
           users.add(get_user(element))       
       
    print len(users)

process_map(SAMPLE_FILE)

