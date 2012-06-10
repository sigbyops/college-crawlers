from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from collegeimages.items import CollegeimagesItem

import urlparse
import fileinput
import os.path

# spider for scraping college images from google images
class CollegeimagesSpider(BaseSpider):
	name = "collegeimages"
	allowed_domains = ["http://en.wikipedia.org"]
	
	# use schools.txt to get all school names
	f = open('collegeimages/spiders/colleges.txt', "r")
	start_urls = ["http://en.wikipedia.org/w/index.php?title=Special%3ASearch&profile=images&search="+url.strip()+"&fulltext=Search" for url in f.readlines()]
	f.close()
		
	def parse(self, response):
		x = HtmlXPathSelector(response)
		
		# find absolute urls for images
		image_rel_urls = x.select('//*[contains(concat( " ", @class, " " ), concat( " ", "searchResultImage", " " ))]//a/img/@src').extract()[0]
		image_abs_urls = urlparse.urljoin(response.url, image_rel_urls.strip())
		
		# find links for images
		links_rel = x.select('//*[contains(concat( " ", @class, " " ), concat( " ", "searchResultImage", " " ))]//a/@href').extract()[0]
		links_abs = urlparse.urljoin(response.url, links_rel)
		
		# store values
		item = CollegeimagesItem()
		item['image_urls'] = [image_abs_urls]
		item['name'] = response.url[response.url.find('search=')+7:response.url.rfind('&fulltext=Search')].replace('+',' ')
		item['links'] = [links_abs]
		return item

