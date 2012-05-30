# Scrapy settings for usnbestcolleges project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'usnbestcolleges'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['usnbestcolleges.spiders']
NEWSPIDER_MODULE = 'usnbestcolleges.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['usnbestcolleges.pipelines.FilePipeline']
