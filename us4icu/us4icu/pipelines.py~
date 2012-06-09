from scrapy import log
import sqlite3

from us4icu.items import Us4IcuItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

# pipeline spider output to a sqlite database
class SQLitePipeline(object):
	
	# this pipeline takes the Item and stuffs it into colleges.sqlite
	def __init__(self):
		self.connection = sqlite3.connect('./colleges.sqlite')
		self.cursor = self.connection.cursor()
		self.cursor.execute('CREATE TABLE IF NOT EXISTS colleges(name TEXT, state TEXT, city TEXT)')

	# take the Item and put it in database
	def process_item(self, item, spider):
		self.cursor.execute("INSERT OR REPLACE INTO colleges(name, state, city) values (?, ?, ?)", (item['name'].strip(), item['state'].strip(), item['city'].strip()))
		self.connection.commit()
		
		log.msg("Item stored: " % item, level=log.DEBUG)
		return item
	
	def handle_error(self, e):
		log.err(e)
