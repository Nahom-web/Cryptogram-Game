import random
import string


class Quote:

    def __init__(self, _quote):
        self.quote = _quote
        self.encoded_quote = ""
        self.encoded_quote_letters = {}
        self.guessed_quote_letters = {}
        self.decoded_quote_letters = {}
        self.uppercase_ascii_letters = string.ascii_uppercase
        ascii_list = list(self.uppercase_ascii_letters)
        random.shuffle(ascii_list)
        self.mixed_ascii = ''.join(ascii_list)

    def encode_letter(self, letter):
        return self.mixed_ascii[self.uppercase_ascii_letters.index(letter.upper())]

    def decode_letter(self, letter):
        return self.uppercase_ascii_letters[self.mixed_ascii.index(letter.upper())]

    def encode_quote(self):
        encoded_str = list(map(lambda s: self.encode_letter(s) if s.isalpha() else s, self.quote))
        self.encoded_quote = "".join(encoded_str)

    def decode_quote(self, _encoded_quote):
        decoded_str = list(map(lambda s: self.decode_letter(s) if s.isalpha() else s, _encoded_quote))
        return "".join(decoded_str)

    def initialize_quote_dictionaries(self):
        for q in range(len(self.encoded_quote)):
            self.encoded_quote_letters[q] = self.encoded_quote[q]
            if self.encoded_quote[q].isalpha():
                self.guessed_quote_letters[q] = "_"
            else:
                self.guessed_quote_letters[q] = self.encoded_quote[q]

    def initialize_decoded_dictionary(self):
        for quote in range(len(self.quote)):
            self.decoded_quote_letters[quote] = self.quote[quote]
