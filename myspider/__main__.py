from parse import Parse
from webcrawler import WebCrawler
from interface import Interface

if __name__ == "__main__":
    interface = Interface()
    parse = Parse()
    args = parse.get_parse()
    parse.do_parse(args)
    webcrawler = WebCrawler(parse)
    webcrawler.get_headers(interface.header_inter())
    webcrawler.get_data(interface.data_inter())
    webcrawler.get_url(interface.url_inter())
    webcrawler.do_crawl()