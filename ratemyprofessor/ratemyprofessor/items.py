# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class RatemyprofessorItem(Item):
    name=Field()
    city=Field()
    region=Field()

class RatemyprofessorinItem(Item):
	name=Field()
	avg=Field()
	tot=Field()
