from usnbestcolleges.items import UsnbestcollegesItem
from pysqlite2 import dbapi2 as sqlite

# pipeline spider output to a text file
class FilePipeline(object):

    def __init__(self):
        self.file = open('rankingsdata.txt', 'wb')

    def process_item(self, item, spider):
		line = item['name'].strip()+','+item['rank'].strip()+','+"Tuition: "+item['tuition'].strip()+','+"Enrollment: "+item['enrollment'].strip()+','+"Freshman Retention: "+item['fresh_retent'].strip()+','+"6-year Graduation: "+item['sixyeargrad_rate'].strip()+'\n'
		self.file.write(line)
		return item
