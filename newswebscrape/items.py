# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewswebscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    heading = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    # image = scrapy.Field()
    date = scrapy.Field()

