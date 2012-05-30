# Author: Joe Lee
# example of a parser

import json
from pprint import pprint

json_data=open('schools.json')
data=json.load(json_data)

# print json data
pprint(data)
json_data.close()
