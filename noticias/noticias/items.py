# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoticiasItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()
    tags = scrapy.Field()
    quantTags = scrapy.Field()
    references = scrapy.Field()
