# by Nahom Haile
# Advanced Topics in Computer Science I
# Letter.py
# Will hold a single letter with it's type: a hint, mistake or a guess

class Letter:

    def __init__(self, _letter, _type="guess"):
        self.letter = _letter
        self.type = _type

    def get_type(self):
        return self.type
