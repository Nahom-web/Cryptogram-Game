

class Quote:

    def __init__(self, _quote, _author="", _difficulty="", _type=""):
        self.quote = _quote
        self.author = _author
        self.difficulty = _difficulty
        self.type = _type

    def get_quote(self):
        return self.quote

    def get_difficulty_level(self):
        return self.difficulty

    def get_author(self):
        return self.author

    def get_type(self):
        return self.type
