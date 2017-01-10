from myspider.webcrawler import WebCrawler
from myspider.parse import Parse


parse = Parse()
parse.get_parse()
webcrawler = WebCrawler(parse)


def test_getheadres():
    with open('test_data/header.txt','r') as f:
        rawheader = f.readlines()
    webcrawler.get_headers(rawheader)


def test_getdata():
    with open('test_data/data.txt','r') as f:
        rawdata = f.readlines()
    webcrawler.get_data(rawdata)

def test_crawl(method):
    webcrawler.do_crawl(method)

def test_url():
    with open('test_data/url.txt','r') as f:
        rawurl = f.readlines()
    webcrawler.get_url(rawurl)


test_getdata()
test_getheadres()
test_url()
test_crawl('GET')