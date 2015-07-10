# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import *

class DoubanFilmSpiderSpider(CrawlSpider):
    name = "douban_film_spider"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "http://movie.douban.com/top250",
    ]
    rules = [
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_item"),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanMoiveItem()

        name = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        director = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        classification = sel.xpath('//span[@property="v:genre"]/text()').extract()
        actor = sel.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()

        # for n in name:
        #     print n
        print(''.join(name))
        item['name'] = ''.join(name)
        item['director'] = ''.join(director)
        item['classification'] = ''.join(classification)
        item['actor'] = ''.join(actor)
        item['year'] = ''.join(sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)'))
        item['score'] = ''.join(sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract())
        item['picture'] = ''.join(sel.xpath('//*[@id="mainpic"]/a/img/@src').extract())
        item['url'] = response.url
        return item
