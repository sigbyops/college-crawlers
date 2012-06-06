from scrapy.item import Item, Field

class Review(Item):
	url=Field() 	# \/[A-Z][A-Z]\/[A-Z]{2,6}\.(html)
	name=Field()	# //*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//b
	grade=Field()	# //*[(@id = "overall_grade")]//font//font[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]
	salary=Field()	# //div[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]
