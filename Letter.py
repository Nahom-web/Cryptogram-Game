# by Nahom Haile
# Advanced Topics in Computer Science I
# Letter.py
# This file includes the Letter class which stores a single letter with it's type: hint, mistake or guess

class Letter:

    def __init__(self, _letter, _type="guess"):
        self.letter = _letter
        self.type = _type

    def get_type(self):
        return self.type
