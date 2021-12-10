# by Nahom Haile
# Advanced Topics in Computer Science I
# Exceptions.py
# This file includes all of the exceptions used for the program


class NoSpaceInBetweenLettersException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, please leave a space between the two letters."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class EmptyGuessException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, you must enter in the decoded letter, a space, then the converted letter."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class EntryToLongException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, you have entered more characters than what was asked for. Please try again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class EntryTooShortException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, you have not entered the required character length. Please try again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class FirstLetterNotALetterException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, first character in entry must be a letter. Please try again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class SecondLetterNotALetterException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, second character in entry must be a letter. Please try again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class CantReceiveHintException(BaseException):
    def __init__(self):
        self.message = "Sorry, you can only receive one hint."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class EncodedLetterIsNotInQuoteException(BaseException):
    def __init__(self):
        self.message = "Sorry, the encoded letter is not in the quote. Please try-again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
