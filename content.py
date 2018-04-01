import re
from ast import literal_eval

class MissedConnections():
    def __init__(self):
        self.c = self.load()

    def load(self):
        content_file = open("craigslist/craigslist_content.txt", "r")
        c = content_file.readlines()
        return c

    def clean_text(self, text):
        try:
            text = re.findall(r'"([^"]*)"', text)[0]
        except IndexError:
            try:
                text = literal_eval(text)[1]
            except IndexError:
                # print(self.c.index(text), (text))
                pass
            pass
        text = text.replace('\\n', '')
        return text

    def content(self):
        return list(map(self.clean_text, self.c))
