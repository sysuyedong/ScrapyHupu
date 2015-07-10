# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import *
import string

class HupuSpider(CrawlSpider):
    name = "hupu_spider"
    allowed_domains = [
        "bbs.hupu.com",
        "my.hupu.com",
    ]
    start_urls = [
        # "http://bbs.hupu.com/bxj",
        "http://my.hupu.com/17306480",
    ]
    rules = [
        # Rule(LinkExtractor(allow=(r'http://bbs.hupu.com/bxj-\d+'))),
        # Rule(LinkExtractor(allow=(r'http://bbs.hupu.com/\d+.html')), callback = "parse_post"),
        Rule(LinkExtractor(allow=(r'http://my.hupu.com/\d+')), callback = "parse_user", follow = True),
        Rule(LinkExtractor(allow=(r'http://my.hupu.com/\d+/following'))),
        Rule(LinkExtractor(allow=(r'http://my.hupu.com/\d+/follower'))),
        # Rule(LinkExtractor(allow=(r'http://my.hupu.com/[\w-]+/photo'))),
        # Rule(LinkExtractor(allow=(r'http://my.hupu.com/\d+/photo/[a-z0-9A-Z-]+.html')), callback = "parse_photo"),
    ]

    # 解析贴子
    def parse_post(self, response):
        sel = Selector(response)
        item = HupuPostItem()

        title = sel.xpath('//*[@id="j_data"]/text()').extract()
        lighten_num = sel.xpath('//*[@id="readfloor"]/div').extract()
        author = sel.xpath('//*[@id="tpc"]/div[2]/div[1]/div[1]/a/text()').extract()
        publish_time = sel.xpath('//*[@id="tpc"]/div[2]/div[1]/div[1]/span[2]/text()').extract()
        url = response.url

        if len(lighten_num) >= 5:
            item['title'] = ''.join(title)
            item['lighten_num'] = len(lighten_num)
            item['author'] = ''.join(author)
            item['publish_time'] = ''.join(publish_time)
            item['url'] = ''.join(url)
            return item
        pass

    # 解析用户
    def parse_user(self, response):
        def get_level_index(info_list):
            index = 1
            for info in info_list:
                for c in info:
                    if c.isdigit():
                        return index
                index = index + 1
            return index

        sel = Selector(response)
        item = HupuUserItem()

        info_list = sel.xpath('//*[@id="main"]/div[1]/div[2]/div/text()').extract()
        level_index = get_level_index(info_list)

        username = sel.xpath('//*[@itemprop="name"]/text()').extract()
        sex = sel.xpath('//*[@itemprop="gender"]/text()').extract()
        place = sel.xpath('//*[@itemprop="address"]/text()').extract()
        level = sel.xpath('//*[@id="main"]/div[1]/div[2]/div/text()[%d]'%(level_index)).extract()
        calorie = sel.xpath('//*[@id="main"]/div[1]/div[2]/div/text()[%d]'%(level_index + 1)).extract()
        online_time = sel.xpath('//*[@id="main"]/div[1]/div[2]/div/text()[%d]'%(level_index + 2)).extract()
        register_time = sel.xpath('//*[@id="main"]/div[1]/div[2]/div/text()[%d]'%(level_index + 3)).extract()
        visit_num = sel.xpath('//*[@id="main"]/div[1]/div[2]/h3/span/text()').extract()
        fans_num = sel.xpath('//*[@id="following"]/p/a[2]/text()').extract()
        follow_num = sel.xpath('//*[@id="following"]/p/a[1]/text()').extract()
        posts_num = sel.xpath('//*[@id="topic"]/p/text()[2]/text()').extract()
        avatar = sel.xpath('//*[@id="j_head"]/@src').extract()
        url = response.url

        visit_num = filter(lambda x: x.isdigit(), ''.join(visit_num))
        fans_num = filter(lambda x: x.isdigit(), ''.join(fans_num))
        follow_num = filter(lambda x: x.isdigit(), ''.join(follow_num))
        posts_num = filter(lambda x: x.isdigit(), ''.join(posts_num))

        if fans_num == "":
            fans_num = 0
        else:
            fans_num = string.atoi(fans_num)

        print fans_num, fans_num >= 10, ''.join(sex), ''.join(sex) == u"\u5973"
        if fans_num >= 10 and ''.join(sex) == u"\u5973":
            item['username'] = ''.join(username)
            item['sex'] = ''.join(sex)
            item['place'] = ''.join(place)
            item['level'] = ''.join(level)
            item['calorie'] = ''.join(calorie)
            item['online_time'] = ''.join(online_time)
            item['register_time'] = ''.join(register_time)
            item['visit_num'] = visit_num
            item['fans_num'] = fans_num
            item['follow_num'] = follow_num
            item['posts_num'] = posts_num
            item['avatar'] = ''.join(avatar)
            item['url'] = ''.join(url)
            return item
        pass

    # 解析相册
    def parse_album(self, response):
        pass

    # 解析相片
    def parse_photo(self, response):
        pass