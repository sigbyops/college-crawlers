# Scrapy settings for ratemyprofessor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ratemyprofessor'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ratemyprofessor.spiders']
NEWSPIDER_MODULE = 'ratemyprofessor.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['ratemyprofessor.pipelines.FilePipeline']
