from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from usnbestcolleges.items import UsnbestcollegesItem

# v.0.3: Parses the first two pages (if there are more than one page)

class RankingsSpider(BaseSpider):
	name = "rankings"
	allowed_domains = ["colleges.usnews.rankingsandreviews.com"]
	start_urls = ["http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data",
		"http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-liberal-arts-colleges/data#",
		"http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/business-overall/data",
		"http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/engineering-doctorate/data",
		"http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/engineering-no-doctorate/data"]
	
	def parse(self, response):
		x = HtmlXPathSelector(response)
        
		# instantiate the item
		item = UsnbestcollegesItem()
       
		# see which url is being searched
		# best national rank
		
		#liberal arts, national
		#if response.url=="http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data" || response.url=="http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-liberal-arts-colleges/data#":
		#page_name = x.select('//h1/text()').extract()
		names = x.select('//*[contains(concat( " ", @class, " " ), concat( " ", "school-name", " " ))]/text()').extract()
		ranks = x.select('//*[contains(concat( " ", @class, " " ), concat( " ", "rankings-score", " " ))]//span/text()').extract()
		tuitions = x.select('//td[contains(concat( " ", @class, " " ), concat( " ", "tuition_display", " " ))]/text()').extract()
		enrollments = x.select('//td[contains(concat( " ", @class, " " ), concat( " ", "total_all_students", " " ))]/text()').extract()
		#accept_rates = x.select('//td[contains(concat( " ", @class, " " ), concat( " ", "r_c_accept_rate", " " ))]/text()').extract()
		fresh_retents = x.select('//td[contains(concat( " ", @class, " " ), concat( " ", "r_c_avg_pct_retention", " " ))]/text()').extract()
		sixyeargrad_rates = x.select('//td[contains(concat( " ", @class, " " ), concat( " ", "r_c_avg_pct_grad_6yr", " " ))]/text()').extract()
		
		# print the data
		i = 0
		#print "%s" % page_name[0].strip()	
		while i<len(names):
			print "%s, %s, %s, %s, %s, %s" % (names[i].strip(), ranks[i].strip(), tuitions[i].strip(), enrollments[i].strip(), fresh_retents[i].strip(), sixyeargrad_rates[i].strip())
			# store information into item
			item['name']=names[i].strip()
			item['rank']=ranks[i].strip()
			item['tuition']=tuitions[i].strip()
			item['enrollment']=enrollments[i].strip()
			item['fresh_retent']=fresh_retents[i].strip()
			item['sixyeargrad_rate']=sixyeargrad_rates[i].strip()
			yield item
			i+=1
		
		nextpage = '//*[(@id = "pagination")]//*[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]/text()'	
		if (len(x.select(nextpage).extract())>0 and x.select(nextpage).extract()[0]=="&gt;"):
			nextpage = x.select('//*[(@id = "pagination")]//*[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]/@href').extract()
			# save the next page link
			nextpagelink = (response.url)[:(response.url).rfind('com',0,len(response.url))+3] + nextpage[0]
			print nextpagelink
			# yield a new request for the next page link
			yield Request(nextpagelink, callback=self.parse)


