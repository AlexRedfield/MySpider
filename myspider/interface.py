import os

basedir = os.path.abspath(__file__)


class Interface(object):

    def __init__(self):
        return

    def header_inter(self):
        with open('data/header.txt', 'r') as f:
            rawheader = f.readlines()
        return rawheader

    def data_inter(self):
        with open('data/data.txt', 'r') as f:
            rawdata = f.readlines()
        return rawdata

    def url_inter(self):
        with open('data/url.txt', 'r') as f:
            rawurl = f.readlines()
        return rawurl