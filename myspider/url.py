# -*- coding:utf-8 -*-


class UrlClass(object):
    """
    url是一个list,其中每个元素(url_dict)是一个dict,每一个dict内含有value(str),method(str),data(list)
    每个url_dict代表了一个url地址,使用的方法和传输数据
    每个value代表了一个url地址
    每个method仅能为POST或者GET
    每个data代表了这个url地址将要传输的所有数据
    """
    def __init__(self, rawurl, data):
        self.url = []
        url_data = data
        for line in rawurl:
            url_dict = {'value': '', 'method': '', 'data': []}
            if line[0] != '#':
                url, method = line.strip().split()
                url_dict['value'] = url
                url_dict['method'] = method
                if method == 'POST':
                    try:
                        url_dict['data'] = url_data.data[url_data.count]
                        url_data.count += 1
                    except IndexError:
                        print "Error!Not enough DATA for POST!"
                self.url.append(url_dict)


class DataClass(object):
    """
    data是一个list,其中每个元素(data_list)是一个list,list内有多组(data_dict)dict
    data所有url的所有POST数据
    每个data_list代表了每个url将POST的所有数据
    每个dict代表了一组POST数据
    """
    def __init__(self, rawdata):
        self.data = []
        data_list = []
        self.count = 0
        for line in rawdata:
            if line[0:3] == '---':
                self.data.append(data_list)
                data_list = []
            elif line[0] != '#':
                data_dict = {}
                line = line.strip()
                data_line = line.split(' ')
                for data_ele in data_line:
                    try:
                        dpre, ddata = data_ele.split(':',1)
                        data_dict[dpre] = ddata
                    except ValueError:
                        print "Error:invalid data format(maybe missing ':'),expect('param:param_data') but('{0}')".format(data_ele)
                data_list.append(data_dict)


class HeaderClass(object):

    def __init__(self, rawheaders):
        self.header = {}
        for line in rawheaders:
            if line[0] != '#':
                line = line.strip()
                try:
                    hpre, hdata = line.split(':', 1)
                    self.header[hpre] = hdata
                except ValueError:
                    print "Error:invalid header format(maybe missing ':'),expect('header:data') but('{0}')".format(line)
