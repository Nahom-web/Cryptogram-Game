import urllib.request as req
from html.parser import HTMLParser
import Quote
import random


class QuoteManager(HTMLParser):

    QUOTE_URL = "https://litemind.com/best-famous-quotes/"

    def __init__(self):
        super().__init__()
        self.reset()
        self.is_quote_div = False
        self.break_line_tag = False
        self.stripped_quotes = list()
        self.quotes = {}

    def handle_starttag(self, tag, attrs):
        self.is_quote_div = False
        self.break_line_tag = False
        if tag == "div":
            for name, value in attrs:
                if name == "class" and value == "wp_quotepage_quote":
                    self.is_quote_div = True
        elif tag == "br":
            self.break_line_tag = True

    def handle_data(self, data):
        if self.is_quote_div:
            self.stripped_quotes.append(data)
        if self.break_line_tag:
            self.stripped_quotes[-1] += f' {data}'

    def parse_url(self):
        with req.urlopen(QuoteManager.QUOTE_URL) as f:
            page_content = list(line.decode("utf-8").strip() for line in f.readlines())
        for line in page_content:
            self.feed(line)

    def create_quotes_dictionary(self):
        for index in range(len(self.stripped_quotes)):
            quote = Quote.Quote(self.stripped_quotes[index][3:].strip())
            self.quotes[index] = quote

    def random_quote(self):
        # randomized_quote = random.choice(list(self.quotes.items()))
        # return randomized_quote[1]
        return self.quotes[0]
