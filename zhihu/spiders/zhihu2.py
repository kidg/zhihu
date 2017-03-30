# -*- coding: utf-8 -*-
import scrapy
from zhihu.settings import USERNAME, PASSWORD

class Zhihu1Spider(scrapy.Spider):
    name = "zhihu1"
    # allowed_domains = ["https://www.zhihu.com/#signin"]
    start_urls = ['https://www.zhihu.com/#signin/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                formdata = {"phone_num":USERNAME, "password":PASSWORD},
                method = "POST",
                url = "https://www.zhihu.com/login/phone_num",
                callback = self.after_login)

    def after_login(self, response):
        # print response.body
        return scrapy.Request("https://www.zhihu.com/", self.parse_index)

    def parse_index(self, response):
        print response.body
