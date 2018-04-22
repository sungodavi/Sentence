import wikipedia
from worksheet import Worksheet
from sentence import Sentence
import random
from nltk import sent_tokenize
import re


pattern = re.compile(r"[\w\d\s.,]+")

class Wikisheet(Worksheet):
    def __init__(self, title=None, size=10):
        super().__init__()
        if title is None:
            page = None
            while page is None:
                try:
                    self.title = wikipedia.random()
                    page = wikipedia.page(self.title).content
                except:
                    pass
        else:
            self.title = title
            page = wikipedia.page(self.title).content

        page = [line for line in sent_tokenize(page) if self._is_valid(line)]
        self.lines = [Sentence(line) for line in random.sample(page, min(size, len(page)))]
        for line in self.lines:
            print(line.doc)

    def _is_valid(self, line):
        return bool(pattern.fullmatch(line))


if __name__ == '__main__':
    sheet = Wikisheet()
    sheet.render()