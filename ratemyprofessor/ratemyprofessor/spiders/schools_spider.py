from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from ratemyprofessor.items import RatemyprofessorItem

class SchoolsSpider(BaseSpider):
	name = "schools"
	allowed_domains = ["ratemyprofessors.com"]
	start_urls = ["http://www.ratemyprofessors.com/SearchSchool.jsp"]
	
	def parse(self, response):
		x = HtmlXPathSelector(response)
       
		# instantiate the item
		item = RatemyprofessorItem()
       
		# save all related fields together from the page
		names = x.select("//*[(@id = 'rmp_table')]//a/text()").extract()
		cities = x.select("//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()").extract()
		regions = x.select("//td[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()").extract()
		
		# print the data
		i = 0
		while i<len(names):
			print "%s, %s, %s" % (names[i], cities[i], regions[i])
			# store information into item
			item['name']=names[i]
			item['city']=cities[i]
			item['region']=regions[i]
			# yield all items (for eventual storing)
			yield item
			i+=1
		
		if len(names)==100:
			page1 = "//a[(((count(preceding-sibling::*) + 1) = 13) and parent::*)]/text()"		
			if (x.select(page1).extract()[0]=="Next"):
				nextpage = x.select("//a[(((count(preceding-sibling::*) + 1) = 13) and parent::*)]/@href").extract()
			else:
				nextpage = x.select("//a[(((count(preceding-sibling::*) + 1) = 12) and parent::*)]/@href").extract()
			# save the next page link
			nextpagelink = (response.url)[:(response.url).rfind('/',0,len(response.url))+1]+nextpage[0]
		
			# yield a new request for the next page link
			yield Request(nextpagelink, callback=self.parse)

		
