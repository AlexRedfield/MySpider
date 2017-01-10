# -*- coding:utf-8 -*-

import requests
from echo import Echo
from analyze import Analyze
from url import DataClass, HeaderClass, UrlClass


class WebCrawler(object):
    """
    网页爬取类
    执行顺序是
    1.get_headers
    2.get_data
    3.get_url
    4.do_crawl
    """
    def __init__(self, parse):
        self.poem = "I saw the light fade from the sky"
        self.resp = ''
        self.cookie = 0
        self.parse = parse
        self.text = ''


    def do_crawl(self):
        """
        执行爬取
        """
        echo = Echo()
        url_count = 0
        url_num = len(self.url.url)
        while url_count < url_num:
            data_count = 0
            url_dict = self.url.url[url_count]
            req = requests.Request(method=url_dict['method'], url=url_dict['value'])

            #加入cookies,data和headers
            if self.parse.cookie_range[2] >= url_count + 1 >= self.parse.cookie_range[1]:
                req.cookies = self.cookie
            if len(url_dict['data']) > data_count:
                req.data = url_dict['data'][data_count]
                data_count += 1

            if len(self.header.header) > 0:
                req.headers = self.header.header

            s = requests.Session()
            prepped = s.prepare_request(req)
            self.resp = s.send(prepped, stream=True)
            if self.resp.status_code == 200:
                if url_count+1 == self.parse.cookie_range[0]:
                    self.cookie = self.resp.cookies
            else:
                print "status_code:{0}".format(self.resp.status_code)

            if data_count == len(url_dict['data']):
                url_count += 1

            #数据分析
            analyze = Analyze(self.parse.analyze_method)
            self.text = analyze.analyze(self.resp.text, self.parse.analyze_rule)


            #输出结果
            if self.parse.echo_method != 'xls':
                #self.text = 'cookies:' + ''.join(self.cookie.values()) + '\n' + 'content:' + self.resp.content + '\n\n' + self.text
                self.text = url_dict['value'] + '\n' + ''.join(str(s) for s in url_dict['data']) + '\n\n' + self.text
                echo.echo(self.parse.echo_method, self.text, url_count, data_count)
            else:
                echo.echo_to_xls(self.text, self.parse.xls_list[0], self.parse.xls_list[1], self.parse.xls_list[2], self.parse.xls_title)


    def get_data(self, rawdata):
        """
        获取参数
        :param rawdata: 如 name:john age:18 gender:man
        :return:
        """
        self.data = DataClass(rawdata)


    def get_headers(self, rawheaders):
        """
        获取请求头
        :param rawheaders: 如 host:www.baidu.com
        :return:
        """
        self.header = HeaderClass(rawheaders)

    def get_url(self, rawurl):
        """
        获取url列表
        :param rawurl:
        :return:
        """
        self.url = UrlClass(rawurl, self.data)

