import urllib.request as req
from html.parser import HTMLParser
import Quote
import random


class QuoteManager(HTMLParser):

    QUOTE_URL = "https://litemind.com/best-famous-quotes/"

    def __init__(self):
        super().__init__()
        self.reset()
        self.class_attribute_name = ""
        self.stripped_quotes = list()
        self.quotes = {}

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for name, value in attrs:
                if name == "class":
                    self.class_attribute_name = value
                else:
                    self.class_attribute_name = ""
        else:
            self.class_attribute_name = ""

    def handle_data(self, data):
        if self.class_attribute_name == "wp_quotepage_quote":
            self.stripped_quotes.append("".join([data[w] for w in range(len(data)) if not data[w].isdigit()])[2:])

    def parse_url(self):
        with req.urlopen(QuoteManager.QUOTE_URL) as f:
            page_content = list(line.decode("utf-8").strip() for line in f.readlines())
        for line in page_content:
            self.feed(line)

    def create_quotes_dictionary(self):
        for index in range(len(self.stripped_quotes)):
            quote = Quote.Quote(self.stripped_quotes[index])
            quote.encode_quote()
            self.quotes[index] = quote

    def random_quote(self):
        randomized_quote = random.choice(list(self.quotes.items()))
        return randomized_quote[1]
