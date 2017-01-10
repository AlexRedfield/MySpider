import bs4
import re

class Analyze(object):

    def __init__(self,method):
        self.method=method

    def analyze(self, text, rule):
        if self.method == 'display':
            return self.analyze_display(text)
        if self.method == 'regeexpr':
            return self.analyze_regexpr(text, rule)

    def analyze_display(self, text):
        return text

    def analyze_regexpr(self, text, rule):
        return re.findall(rule, text)
