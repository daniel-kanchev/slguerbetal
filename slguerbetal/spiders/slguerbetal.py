import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from slguerbetal.items import Article


class SlguerbetalSpider(scrapy.Spider):
    name = 'slguerbetal'
    start_urls = ['https://www.slguerbetal.ch/de/']

    def parse(self, response):
        articles = response.xpath('//article')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            title = article.xpath('./h2//text()').get()

            content = article.xpath('./div[@class="long-text"]//text()').getall()
            content = [text for text in content if text.strip()]
            content = "\n".join(content).strip()

            item.add_value('title', title)
            item.add_value('content', content)

            yield item.load_item()



