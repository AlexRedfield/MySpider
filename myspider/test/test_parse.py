from myspider.parse import  Parse

parse = Parse()

def test_parse():
    args = parse.get_parse()
    print args
    parse.do_parse(args)

test_parse()