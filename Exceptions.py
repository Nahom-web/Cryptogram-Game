# by Nahom Haile
# Advanced Topics in Computer Science I
# Exceptions.py
# Contains all the exceptions used within the program


class NoSpaceInBetweenConversionException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, please leave a space between the two letters."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class MoreThanTwoLettersException(BaseException):
    def __init__(self):
        self.message = "Invalid conversion, you can only enter in two letters. First the decoded letter, " \
                       "then a space, then a letter to replace with. "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidCharactersInConversionException(BaseException):
    def __init__(self):
        self.message = "Invalid characters, you cannot convert a letter to an invalid character. Please try again"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class OneLetterWhenConvertingException(BaseException):
    def __init__(self):
        self.message = "Invalid conversion, you are not allowed to enter in one letter. Please try again"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class NumbersInGuessException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, you are not allowed to enter in numbers for your conversion. Please try again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class EmptyGuessException(BaseException):
    def __init__(self):
        self.message = "Invalid entry, you must enter in the decoded letter, a space, then the converted letter."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class CannotConvertToNumberException(BaseException):
    def __init__(self):
        self.message = "Invalid conversion, you cannot convert a letter to a number. Please try again."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class CannotConvertNumberToLetterException(BaseException):
    def __init__(self):
        self.message = "Invalid conversion, you convert a number to a letter. Please try again."
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
