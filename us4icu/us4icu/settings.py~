# Scrapy settings for us4icu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'us4icu'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['us4icu.spiders']
NEWSPIDER_MODULE = 'us4icu.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['us4icu.pipelines.SQLitePipeline']
