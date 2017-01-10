import argparse

class Parse(object):

    def __init__(self):
        self.echo_method = 'screen'
        self.cookie_range = [-1, -1, -1]
        self.echo_range = [0, 99999]
        self.xls_list = []
        self.xls_title = []
        return

    def get_parse(self):
        parser = argparse.ArgumentParser(description="Welcome to ues Myspider!")
        parser.add_argument('-c', default='false', nargs=3, help='-c n1 n2 n3 | cookies from n1st url will be sent to urls from a range of n2st to n3st')
        parser.add_argument('-e', default='false', nargs='*', help='-e method n1 n2 | \'method\' includes \'screen\'(print to screen) \'file\'(print to file)\
                                                                     | \'n1,n2\' is a range from n1 to n2 of url to be echoed')
        parser.add_argument('-x', default='false', nargs='*', help='-x name_of_xls, name_of_sheet, column, *title\n\
                                                                | for example: student_score.xls score 4 name,age,gender,score')
        p = parser.parse_args('-c 2 3 3 -e file'.split())

        return vars(p)

    def args_cookie(self, argv):
        try:
            self.cookie_range[0] = int(argv[0])
            self.cookie_range[1] = int(argv[1])
            self.cookie_range[2] = int(argv[2])
        except TypeError:
            print "Error:invalid range format, expect(n1,n2,n3) but({0})".format(argv)
        #debug
        #print ("cookie:",self.cookie_range)

    def args_echo(self, argv):
        self.echo_method = argv[0]
        if len(argv) == 3:
            try:
                self.echo_range.append(int(argv[1]))
                self.echo_range.append(int(argv[2]))
            except TypeError:
                print "Error:invalid range format, expect(n1,n2) but({0})".format(argv)
        #debug
        #print ("echo:"+self.echo_method,self.echo_range)

    def args_xls(self, argv):
        self.xls_list = argv
        self.xls_title = argv[3].split(',')
        try:
            self.xls_list[2] = int(self.xls_list[2])
        except TypeError:
            print "Error:invalid type, expect number in str, but({0})".format(self.xls_list[2])
        #debug
        #print ("xls:",self.xls_list,self.xls_title)

    def do_parse(self, args):
        if args['e'] != 'false':
            self.args_echo(args['e'])
        if args['c'] != 'false':
            self.args_cookie(args['c'])
        if args['x'] != 'false':
            self.args_xls(args['x'])

