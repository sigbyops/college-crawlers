from ratemyprofessor.items import RatemyprofessorItem
from ratemyprofessor.items import RatemyprofessorinItem

from scrapy import log
import sqlite3

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
			
# pipeline spider output to a sqlite database
class SQLitePipeline(object):
	
	# this pipeline takes the Item and stuffs it into ratings.sqlite
	def __init__(self):
		self.connection = sqlite3.connect('./ratings.sqlite')
		self.cursor = self.connection.cursor()
		self.cursor.execute('CREATE TABLE ratings(name TEXT, avg REAL, total INTEGER )')

	# take the Item and put it in database
	def process_item(self, item, spider):
		self.cursor.execute("insert into ratings(name, avg, total) values (?, ?, ?)", (item['name'][0].strip(), item['avg'][0].strip(), item['tot'][0].strip()))
		self.connection.commit()
		
		log.msg("Item stored: " % item, level=log.DEBUG)
		return item
	
	def handle_error(self, e):
		log.err(e)
		

