tags = {}

def count_tags(SAMPLE_FILE):
        
        for event, elem in ET.iterparse(SAMPLE_FILE):
            if elem.tag in tags.keys():
                tags[elem.tag]+= 1
            else:
                tags[elem.tag] = 1
                
count_tags(SAMPLE_FILE)        
print tags
