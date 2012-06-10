from collegeimages.items import CollegeimagesItem

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

from scrapy import log
import sqlite3

# Custom Images Pipeline (overriding methods from ImagesPipeline)
class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

# pipeline spider output to a sqlite database
class SQLitePipeline(object):
	
	# this pipeline takes the Item and stuffs it into colleges.sqlite
	def __init__(self):
		self.connection = sqlite3.connect('./collegeimages.sqlite')
		self.cursor = self.connection.cursor()
		self.cursor.execute('CREATE TABLE IF NOT EXISTS collegeimages(name TEXT, image TEXT, link TEXT)')

	# take the Item and put it in database
	def process_item(self, item, spider):
		self.cursor.execute("INSERT OR REPLACE INTO collegeimages(name, image, link) values (?, ?, ?)", (item['name'].strip(), item['image_urls'][0].strip(), item['links'][0].strip()))
		self.connection.commit()
		
		log.msg("Item stored: " % item, level=log.DEBUG)
		return item
	
	def handle_error(self, e):
		log.err(e)
