# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


from ratemyprofessor.items import RatemyprofessorItem
from ratemyprofessor.items import RatemyprofessorinItem

# pipeline spider output to a text file
class FilePipeline(object):

    def __init__(self):
        self.file = open('schools.txt', 'wb')

    def process_item(self, item, spider):
		if isinstance(item, RatemyprofessorItem):
			line = item['name'].strip() + ', ' + item['city'].strip() + ', ' + item['region'].strip() + '\n'
			self.file.write(line)
			return item
		if isinstance(item, RatemyprofessorinItem):
			line = item['name'][0].strip() + ', ' + 'Avg: ' + item['avg'][0].strip() + ', ' + 'Total #: ' + item['tot'][0].strip() + '\n'
			self.file.write(line)
			return item
