# -*- coding: utf-8 -*-
import scrapy
from zhihu.settings import USERNAME, PASSWORD

class Zhihu1Spider(scrapy.Spider):
    name = "zhihu2"
    # allowed_domains = ["https://www.zhihu.com/#signin"]
    start_urls = ['https://www.zhihu.com/#signin/']

    def parse(self, response):

        cookies = {
        "q_c1":"124a855e77fb492fba849480e0bd14a8|1490676062000|1486208258000",
        "d_c0":"AFCCuz9OQguPTkWBFS6r - YtUxvGy2MEHBXc = | 1486208258",
        "__utma":"51854390.1719296171.1486208260.1490860967.1490873343.5",
        "__utmz":"51854390.1486208260.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
        "__utmv":"51854390.100--|2=registration_date=20150815=1^3=entry_date=20150815=1",
        "r_cap_id":"YmVkYTNlMDBmMWY3NGM2OWE4OTZlMjUwMjQ2ZmRhMmQ = | 1490862755 | a61adcc60dbe06bcea07621a43ce9f297d359547",
        "cap_id":"MmJmMTZmMmM3MWUwNDA3MzhjYzZlMzA5ZjkzOGY2NTE = | 1490862755 | 2ffe323c4a743ffd0b2da6946a631bec32f92ccf",
        "_zap":"3de1bf83-014c-40f0-8814-9a8565909da3",
        "aliyungf_tc":"AQAAAN+A4mhFMQMAGsC3PbRaFzl6upl+",
        "l_n_c":1,
        "_xsrf":"372d813b66ce7355c16e3b48201d1cdd",
        "__utmc":51854390,
        "z_c0":"Mi4wQUJCTWp0WGppd2dBVUlLN1AwNUNDeGNBQUFCaEFsVk4tMUFFV1FDWVAwTjNTWlRSbU8xTE5lNnQxTU1CS0VxdS13|1490876412|b651ce28306424285c09252259121b2961883b95",
        "__utmb":"51854390.0.10.1490873343",
            }
        yield scrapy.Request("https://www.zhihu.com/", self.home, cookies=cookies)

    def home(self, response):
        # print response.body
        # print response.headers["Set-Cookie"]
        # pattern1 = '//div[starts-with(@class,"feed-item folding feed-item-hook feed-item")]'
        pattern1 = '//div[starts-with(@id,"feed")]'
        pattern2 = './div/div[2]/div[2]/h2/a/text()'
        pattern3 = './div/div[2]/div[2]/div/div[5]/div/text()'
        for item in response.xpath(pattern1):
            # print item
            title = item.xpath(pattern2).extract()[0] if item.xpath('./div/div[2]/div[2]/div') else ""
            content = item.xpath(pattern3).extract()[0] if item.xpath('./div/div[2]/div[2]/div') else ""
            print "The title is:" + title
            print "The content is:" + content
