# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class UsnbestcollegesItem(Item):
	name=Field()
	rank=Field()
	tuition=Field()
	enrollment=Field()
	fresh_retent=Field()
	sixyeargrad_rate=Field()
