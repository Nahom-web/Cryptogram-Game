# by Nahom Haile
# Advanced Topics in Computer Science I
# QuoteManager.py
# Contains the html parser class and create a dictionary of the parsed quotes from the famous quotes website

import urllib.request as req
from html.parser import HTMLParser
import Quote
import random


class QuoteManager(HTMLParser):

    QUOTE_URL = "https://litemind.com/best-famous-quotes/"

    def __init__(self):
        super().__init__()
        self.reset()
        self.is_quote = False
        self.check_quote_end_tag = False
        self.stripped_quotes = list()
        self.quotes = {}

    def handle_starttag(self, tag, attrs):
        self.is_quote = False
        if tag == "div":
            for name, value in attrs:
                if name == "class" and value == "wp_quotepage_quote":
                    self.is_quote = True
                    self.check_quote_end_tag = True

    def handle_endtag(self, tag):
        if self.check_quote_end_tag:
            self.check_quote_end_tag = False

    def handle_data(self, data):
        if self.is_quote:
            self.stripped_quotes.append(data)
        elif self.check_quote_end_tag:
            self.stripped_quotes[-1] += f' {data}'

    def parse_url(self):
        with req.urlopen(QuoteManager.QUOTE_URL) as f:
            page_content = list(line.decode("utf-8").strip() for line in f.readlines())
        for line in page_content:
            self.feed(line)

    def create_quotes_dictionary(self):
        for index in range(len(self.stripped_quotes)):
            quote = Quote.Quote(self._remove_number_from_quote(self.stripped_quotes[index]))
            self.quotes[index] = quote

    def _remove_number_from_quote(self, quote):
        start_point = [q for q in range(len(quote)) if quote[q].isalpha()][0]
        return quote[start_point:]

    def random_quote(self):
        randomized_quote = random.choice(list(self.quotes.items()))
        return randomized_quote[1]
