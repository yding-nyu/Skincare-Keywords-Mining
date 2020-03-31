# -*- coding: utf-8 -*-
import scrapy
from scrapyspider.items import ScrapyspiderItem
from scrapy.selector import Selector


class DermstoreSpiderSpider(scrapy.Spider):
    name = 'dermstore_spider'
    allowed_domains = ['www.dermstore.com']
    start_urls = ['https://www.dermstore.com/blog/category/skin/']

    def parse(self, response):
        urls_list = response.xpath("//meta[@itemprop ='url']//@content").extract()
        for url in urls_list:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        item = ScrapyspiderItem()
        selector = Selector(response)
        item['url'] = response.url
        item['title'] = selector.xpath("//h1[@class ='postTitle']/text()").extract_first()
        item['author'] = selector.xpath("//p[@class='postDetails']/text()").extract_first()
        content = selector.xpath("//p[@style='text-align: justify;']/text()").extract()
        item['content'] = "".join(content)
        yield item

