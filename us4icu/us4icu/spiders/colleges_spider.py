from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from us4icu.items import Us4IcuItem

class CollegesSpider(CrawlSpider):
	name = "colleges"
	allowed_domains = ["4icu.org"]
	start_urls = ["http://www.4icu.org/us/"]
	
	rules = (
		Rule(SgmlLinkExtractor(allow=('\/[A-Z][a-z]+\.(htm)', )), callback='parse_page'),
	)
	
	def parse_page(self, response):
		x = HtmlXPathSelector(response)
		
		# instantiate item
		item = Us4IcuItem()
		
		# use xpath to store arrays of fields
		names = x.select('//*[contains(concat( " ", @class, " " ), concat( " ", "i", " " ))]//a/text()').extract()
		cities = x.select('//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//h6/text()').extract()
		
		# store item fields
		item['state'] = (response.url)[(response.url).rfind('/',0,len(response.url))+1:(response.url).rfind('.',0,len(response.url))].replace('-',' ')
		
		for name,city in zip(names,cities):
			item['name'] = name
			if '...' in city:
				item['city'] = city[:city.rfind('...')]
			else:
				item['city'] = city
			print item['name']
			print item['city']
			print item['state']
			yield item

