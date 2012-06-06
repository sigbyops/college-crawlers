from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import Review

class DmozSpider(BaseSpider):
	name = "dmoz"
   allowed_domains = ["studentsreview.com"]
   start_urls = [
		 "http://www.studentsreview.com/NY/CUNYBAC.html",
       "http://www.studentsreview.com/IN/RIT.html",
       "http://www.studentsreview.com/OH/MUO.html",
       "http://www.studentsreview.com/MI/UMAA.html",
       "http://www.studentsreview.com/OH/CWT.html",
       "http://www.studentsreview.com/NY/SUNYA.html"
	]

	def parse(self, response):
       x = HtmlXPathSelector(response)
       
       item = Review()
       item['url'] = response.url
       item['name'] = x.select("//descendant-or-self::*[contains(concat(' ', normalize-space(@class), ' '), ' title ')]/descendant::b/text()").extract()
       item['grade'] = x.select("//*[(@id = 'overall_grade')]//font//font[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()").extract()
       item['salary'] = x.select("//div[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()").extract()
       
       
       return item
       
