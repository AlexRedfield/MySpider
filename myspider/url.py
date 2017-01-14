# -*- coding:utf-8 -*-
URLINDEX = 0
METHODINDEX = 1
TYPEINDEX = 2
REINDEX = 3

class UrlClass(object):
    """
    url是一个list,其中每个元素(url_dict)是一个dict,每一个dict内含有value(str),method(str),data(list)
    每个url_dict代表了一个url地址,使用的方法和传输数据
    每个value代表了一个url地址
    每个method仅能为POST或者GET
    每个data代表了这个url地址将要传输的所有数据
    每个text代表了这个url请求后得到的数据
    """
    def __init__(self, rawurl, data):
        self.url = []
        addparam = []
        url_data = data
        for line in rawurl:
            re_text = ''
            url = ''
            method = ''
            type = ''
            url_dict = {'value': '', 'method': '', 'data': [], 'text': [], 'addparam': [], 're': '', 'type': ''}
            if line[0] != '#':
                try:
                    if ' re:' in line:
                        line, re_text = line.strip().split(' re:')
                    line_list = line.strip().split(' ')
                    url = line_list[URLINDEX]
                    method = line_list[METHODINDEX]
                    type = line_list[TYPEINDEX]
                    if (len(line_list) >= REINDEX + 1):
                        paramtrans = line_list[REINDEX:]
                        for ele in paramtrans:
                            addparam = ele.split(':')
                            url_dict['addparam'].append(addparam)
                except ValueError:
                    print "Error!Invalid url format, expect([URL method [re:rule] [index:param]]) but({0})".format(line)
                except IndexError:
                    print "Error!List index out of range, make sure text isn't empty!"
                url_dict['value'] = url
                url_dict['method'] = method
                url_dict['re'] = re_text
                url_dict['type'] = type
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
