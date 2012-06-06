from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from petersons.items import PetersonsItem
from petersons.items import PetersonsinItem

class PetersonsSpider(BaseSpider):
	name = "majors"
	allowed_domains = ["petersons.com"]
	start_urls = ["http://www.petersons.com/college-search/search-by-major.aspx"]
	
	def parse_major(self, response):
		x = HtmlXPathSelector(response)
		
		itemz = PetersonsinItem()
		
		itemz['name'] = x.select('//*[contains(concat( " ", @class, " " ), concat( " ", "results_left", " " ))]//a/text()').extract()
		
		nextpage = x.select('//li[(((count(preceding-sibling::*) + 1) = 12) and parent::*)]//a/@href').extract()
		print nextpage
		#nexturl = response.url[:(response.url).find("college-search")-1] + nextpage[0]	

		#yield itemz
		#yield Request(nexturl, callback=self.parse_major)
		

		
	def parse(self, response):
		x = HtmlXPathSelector(response)
       
		# instantiate the item
		item = PetersonsItem()
       
		# save all related fields together from the page
		majors = x.select("//*[(@id = 'col_a')]//a/text()").extract()
		majorslinks = x.select("//*[(@id = 'col_a')]//a/@href").extract()

		(majors).sort()
		i = 0
		while i<1:
			#print "Major: %s" % majors[i]
			#item[major] = majors[i]
			
			majorurl = majorslinks[i]
			yield Request(majorurl, callback=self.parse_major)
			
			#yield item
			i += 1
		
