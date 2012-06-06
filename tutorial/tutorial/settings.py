# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tutorial'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
DEFAULT_ITEM_CLASS = 'tutorial.items.Review'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

#ITEM_PIPELINES = ['tutorial.pipelines.FilterWordsPipeline']

