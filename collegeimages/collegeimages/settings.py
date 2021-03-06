# Scrapy settings for collegeimages project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'collegeimages'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['collegeimages.spiders']
NEWSPIDER_MODULE = 'collegeimages.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

#ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
ITEM_PIPELINES = ['collegeimages.pipelines.SQLitePipeline']
#IMAGES_STORE = 'images'
#IMAGES_EXPIRES = 60 # images expire in 2 months
#IMAGES_THUMBS = {
#    'small': (100, 100),
    #'big': (270, 270),
#}
#IMAGES_MIN_HEIGHT = 100
#IMAGES_MIN_WIDTH = 100
