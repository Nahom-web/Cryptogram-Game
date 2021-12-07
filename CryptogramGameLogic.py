import Exceptions
import string
import random
import Letter


class CryptogramGameLogic:

    def __init__(self, _quote_chosen):
        self.quote_chosen = _quote_chosen
        self.time_taken = 0
        self.encoded_quote = ""
        self.encoded_quote_letters = {}
        self.guessed_quote_letters = {}
        self.guessed_letters = list()
        self.decoded_quote_letters = {}
        self.alphabet = {}
        self.number_of_hints = 0
        self.uppercase_ascii_letters = string.ascii_uppercase
        ascii_list = list(self.uppercase_ascii_letters)
        random.shuffle(ascii_list)
        self.mixed_ascii = ''.join(ascii_list)

    def create_alphabet_dictionary(self):
        for letter in range(len(self.uppercase_ascii_letters)):
            self.alphabet[self.uppercase_ascii_letters[letter]] = Letter.Letter("_")

    def encode_letter(self, letter):
        return self.mixed_ascii[self.uppercase_ascii_letters.index(letter.upper())]

    def decode_letter(self, letter):
        return self.uppercase_ascii_letters[self.mixed_ascii.index(letter.upper())]

    def encode_quote(self):
        encoded_str = list(map(lambda s: self.encode_letter(s) if s.isalpha() else s, self.quote_chosen))
        self.encoded_quote = "".join(encoded_str)

    def decode_quote(self, _encoded_quote):
        decoded_str = list(map(lambda s: self.decode_letter(s) if s.isalpha() else s, _encoded_quote))
        return "".join(decoded_str)

    def initialize_quote_dictionaries(self):
        for q in range(len(self.encoded_quote)):
            self.encoded_quote_letters[q] = Letter.Letter(self.encoded_quote[q])
            if self.encoded_quote[q].isalpha():
                self.guessed_quote_letters[q] = Letter.Letter("_")
            else:
                self.guessed_quote_letters[q] = Letter.Letter(self.encoded_quote[q])

    def initialize_decoded_dictionary(self):
        for quote in range(len(self.quote_chosen)):
            self.decoded_quote_letters[quote] = Letter.Letter(self.quote_chosen[quote].upper())

    def check_guess_length(self, guess):
        if len(guess) > 3:
            raise Exceptions.EntryToLongException()
        elif len(guess) < 3:
            raise Exceptions.EntryTooShortException()
        return True

    def check_guessed_quote(self):
        for i, v in self.guessed_quote_letters.items():
            if v.letter == "_":
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
            first_letter = guess[:1].upper()
            self.check_first_letter(first_letter)

            space = guess[1:2]
            self.check_white_space(space)

            second_letter = guess[1:].strip().upper()
            if second_letter != "_":
                self.check_second_letter(second_letter)

            self.alphabet[first_letter].letter = second_letter
            self.guessed_letters.append(second_letter)
            self.update_quote(first_letter, second_letter)

    def update_quote(self, encoded_letter, letter, hint=False):
        indexes = list()
        for index, value in self.encoded_quote_letters.items():
            if value.letter == encoded_letter:
                indexes.append(index)
        for i in indexes:
            self.guessed_quote_letters[i].letter = letter
            self.guessed_quote_letters[i].type = "guess"
            if hint:
                self.guessed_quote_letters[i].type = "hint"

    def can_receive_hint(self):
        return self.number_of_hints == 0

    def receive_hint(self):
        self.number_of_hints += 1
        given_letter = ""
        for index, letter in self.decoded_quote_letters.items():
            if letter.letter.isalpha():
                if letter not in self.guessed_letters:
                    given_letter = letter.letter.strip()
                    continue
        self.update_quote(self.encode_letter(given_letter), given_letter, hint=True)
        self.alphabet[self.encode_letter(given_letter)].letter = given_letter

    def update_alphabet(self, letter):
        self.alphabet[letter].letter = "_"

    def update_guessed_letters(self, letter):
        if letter in self.guessed_letters:
            self.guessed_letters.remove(letter)

    def remove_guessed_letter(self, index):
        self.guessed_quote_letters[index].type = "mistake"

    def find_all_mistakes(self):
        for index in range(len(self.guessed_quote_letters)):
            letter_to_remove = self.guessed_quote_letters[index].letter
            if letter_to_remove.isalpha():
                if letter_to_remove != self.decoded_quote_letters[index].letter:
                    # self.update_alphabet(letter_to_remove)
                    # self.update_guessed_letters(letter_to_remove)
                    self.remove_guessed_letter(index)

    @staticmethod
    def convert_letter_objects_to_list(dictionary_of_letter_objects):
        letters = list()
        for index, letter in dictionary_of_letter_objects.items():
            letters.append(letter.letter)
        return letters

    def is_win(self):
        return self.convert_letter_objects_to_list(self.guessed_quote_letters) == self.convert_letter_objects_to_list(self.decoded_quote_letters)

    def is_game_over(self):
        letter_in_guessed_quote = list()
        for index, letter in self.guessed_quote_letters.items():
            letter_in_guessed_quote.append(letter.letter)
        return '_' not in self.convert_letter_objects_to_list(self.guessed_quote_letters)
