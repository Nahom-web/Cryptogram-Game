import Exceptions


class CryptogramGameLogic:

    def __init__(self, _quote_chosen):
        self.quote_chosen = _quote_chosen
        self.time_taken = 0

    def check_guess_length(self, guess):
        if len(guess) > 3:
            raise Exceptions.EntryToLongException()
        elif len(guess) < 3:
            raise Exceptions.EntryTooShortException()
        return True

    def check_guessed_quote(self):
        for i, v in self.quote_chosen.guessed_quote_letters.items():
            if v == "_":
                return False
        return True

    def check_first_letter(self, letter):
        if not letter.isalpha():
            raise Exceptions.FirstLetterNotALetterException()

    def check_white_space(self, white_space):
        if white_space != " ":
            raise Exceptions.NoSpaceInBetweenConversionException()

    def check_second_letter(self, letter):
        if not letter.isalpha():
            raise Exceptions.SecondLetterNotALetterException()

    def determine_guess(self, guess):
        if self.check_guess_length(guess):
            first_letter = guess[:1]
            self.check_first_letter(first_letter)

            space = guess[1:2]
            self.check_white_space(space)

            second_letter = guess[1:].strip()
            if second_letter != "_":
                self.check_second_letter(second_letter)

            self.update_quote(first_letter, second_letter)

    def update_quote(self, encoded_letter, letter):
        indexes = list()
        for index, value in self.quote_chosen.encoded_quote_letters.items():
            if value == encoded_letter:
                indexes.append(index)
        for i in indexes:
            self.quote_chosen.guessed_quote_letters[i] = letter

    def get_hint(self):
        pass

    def find_all_mistakes(self):
        pass

    def is_win(self):
        pass

