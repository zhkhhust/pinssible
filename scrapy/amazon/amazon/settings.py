# -*- coding: utf-8 -*-

# Scrapy settings for amazon project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'


ITEM_PIPELINES = {
	'amazon.pipelines.DuplicatesPipeline': 200,
	'amazon.pipelines.AmazonPipeline'    : 300,
#	'ccc.pipelines.JsonWriterPipeline': 300,
#	'ccc.pipelines.JsonWriterPipeline': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amazon (+http://www.yourdomain.com)'
