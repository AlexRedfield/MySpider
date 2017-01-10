import bs4
import re

class Analyze(object):

    def __init__(self):
        return

    def analyze(self, text, rule):
        if rule == '':
            return self.analyze_display(text)
        else:
            return self.analyze_regexpr(text, rule)

    def analyze_display(self, text):
        disp_list = []
        disp_list.append(text)
        return disp_list

    def analyze_regexpr(self, text, rule):
        return re.findall(rule, text)
