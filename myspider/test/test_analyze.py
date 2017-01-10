from myspider.analyze import Analyze

text = 'q23rjfkjt9032u4jr3849612_)*&nbb'
rule = '\\d{4}'
analyze1 = Analyze('display')
analyze2 = Analyze('regeexpr')

def test_analyze(analyze, text, rule):
    print analyze.analyze(text, rule)

test_analyze(analyze1, text, rule)
test_analyze(analyze2, text, rule)