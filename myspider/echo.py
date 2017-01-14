# -*- coding:utf-8 -*-

import xlwt
import os
import time


class Echo(object):

    def __init__(self):
        self.echo_mkdir()

    def echo(self, method,pretext, text, type, url_count, data_count):
        if method == 'screen':
            self.echo_to_screen(text)
        if method == 'file':
            self.echo_to_file(pretext, text, type, url_count, data_count)

    def echo_to_screen(self, text):
        #加入encode
        print text.encode('utf-8')

    def echo_to_file(self, pretext, text, type, url_count, data_count):
        if type == 't':
            with open(self.file_name+'/result_url'+str(url_count)+'_'+str(data_count)+'.txt', 'w') as result:
                result.writelines(pretext.encode('utf-8'))
                result.writelines(text.encode('utf-8'))
                result.close()
        elif type == 'b':
            with open(self.file_name + '/' + pretext, 'wb') as result:
                for chunk in text:
                    result.write(chunk)
                result.close()

    def echo_to_xls(self, text, name_of_xls, name_of_sheet, column, *title):
        """
        输出到xls文件
        :param text: 格式需满足 row行 column列 每个元素以空格隔开
        :param column: 列数
        :param name_of_sheet: 表单名(仅支持单页)
        :param title: 第0行每一列标题
        :return:
        """
        row = 0

        wb = xlwt.Workbook(encoding='utf-8')
        sheet = wb.add_sheet(name_of_sheet, cell_overwrite_ok=True)
        for i in range(0, column):
            sheet.write(0, i, title[i])

        for line in text:
            row += 1
            ele_column = 0
            line=line.strip()
            data_dict = line.split(' ')
            for element in data_dict:
                try:
                    sheet.write(row, ele_column, element)
                    ele_column += 1
                except:
                    print 'Error:failed to write into {0}'.format(name_of_xls)

        wb.save(name_of_xls)

    def echo_mkdir(self):
        self.file_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        if not os.path.exists(self.file_name):
            os.mkdir(self.file_name)
