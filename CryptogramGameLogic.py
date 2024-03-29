# by Nahom Haile
# Advanced Topics in Computer Science I
# CryptogramGameLogic.py
# The file includes the CryptogramGameLogic class which contains all the cryptogram logic


import Exceptions
import string
import random
import Letter
import time
from colorama import Fore


class CryptogramGameLogic:

    def __init__(self, _quote_chosen):
        self.quote_chosen = _quote_chosen
        self.start_time = time.time()
        self.end_time = 0
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

    def _encode_letter(self, letter):
        return self.mixed_ascii[self.uppercase_ascii_letters.index(letter.upper())]

    def _decode_letter(self, letter):
        return self.uppercase_ascii_letters[self.mixed_ascii.index(letter.upper())]

    def encode_quote(self):
        encoded_str = list(map(lambda s: self._encode_letter(s) if s.isalpha() else s, self.quote_chosen))
        self.encoded_quote = "".join(encoded_str)

    def _decode_quote(self, _encoded_quote):
        decoded_str = list(map(lambda s: self._decode_letter(s) if s.isalpha() else s, _encoded_quote))
        return "".join(decoded_str)

    def initialize_quote_dictionaries(self):
        for q in range(len(self.encoded_quote)):
            self.encoded_quote_letters[q] = Letter.Letter(self.encoded_quote[q])
            if self.encoded_quote[q].isalpha():
                self.guessed_quote_letters[q] = Letter.Letter("_")
            else:
                self.guessed_quote_letters[q] = Letter.Letter(self.encoded_quote[q])

    def initialize_decoded_dictionary_of_quote_letters(self):
        for quote in range(len(self.quote_chosen)):
            self.decoded_quote_letters[quote] = Letter.Letter(self.quote_chosen[quote].upper())

    def _check_guess_length(self, guess):
        if len(guess) > 3:
            raise Exceptions.EntryToLongException()
        elif len(guess) < 3:
            raise Exceptions.EntryTooShortException()
        return True

    def _check_guessed_quote(self):
        for i, v in self.guessed_quote_letters.items():
            if v.letter == "_":
                return False
        return True

    def _check_first_letter(self, letter):
        if not letter.isalpha():
            raise Exceptions.FirstLetterNotALetterException()

    def _check_white_space(self, white_space):
        if white_space != " ":
            raise Exceptions.NoSpaceInBetweenLettersException()

    def _check_second_letter(self, letter):
        if not letter.isalpha():
            raise Exceptions.SecondLetterNotALetterException()

    def _check_if_letter_is_in_quote(self, letter):
        guessed_letters = self.letter_objects_to_list_of_letters(self.encoded_quote_letters)
        if letter not in guessed_letters:
            raise Exceptions.EncodedLetterIsNotInQuoteException()

    def determine_guess(self, guess):
        if self._check_guess_length(guess):
            first_letter = guess[:1].upper()
            self._check_first_letter(first_letter)

            space = guess[1:2]
            self._check_white_space(space)

            second_letter = guess[1:].strip().upper()
            if second_letter != "_":
                self._check_second_letter(second_letter)

            self._check_if_letter_is_in_quote(first_letter)
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
        if self.number_of_hints == 0:
            self._receive_hint()
        else:
            raise Exceptions.CantReceiveHintException()

    def _receive_hint(self):
        self.number_of_hints += 1
        given_letter = ""
        for index, letter in self.decoded_quote_letters.items():
            if letter.letter.isalpha():
                if letter.letter not in self.guessed_letters:
                    given_letter = letter.letter.strip()
                    break
        self.update_quote(self._encode_letter(given_letter), given_letter, hint=True)
        self.alphabet[self._encode_letter(given_letter)].letter = given_letter

    def _update_alphabet(self, letter):
        self.alphabet[letter].letter = "_"

    def _update_guessed_letters(self, letter):
        if letter in self.guessed_letters:
            self.guessed_letters.remove(letter)

    def set_letter_as_mistake(self, index):
        self.guessed_quote_letters[index].type = "mistake"

    def find_all_mistakes(self):
        for index in range(len(self.guessed_quote_letters)):
            letter_to_remove = self.guessed_quote_letters[index].letter
            if letter_to_remove.isalpha():
                if letter_to_remove != self.decoded_quote_letters[index].letter:
                    self.set_letter_as_mistake(index)

    def remove_all_mistakes(self):
        for index in range(len(self.guessed_quote_letters)):
            if self.guessed_quote_letters[index].type == "mistake":
                self._update_alphabet(self.guessed_quote_letters[index].letter)
                self._update_guessed_letters(self.guessed_quote_letters[index].letter)
                self.guessed_quote_letters[index].letter = "_"
                self.guessed_quote_letters[index].type = "guess"

    @staticmethod
    def letter_objects_to_list_of_letters(dictionary_of_letter_objects):
        letters = list()
        for index, letter in dictionary_of_letter_objects.items():
            letters.append(letter.letter)
        return letters

    @staticmethod
    def letter_objects_to_list_of_letter_types(dictionary_of_letter_objects):
        letters = list()
        for index, letter in dictionary_of_letter_objects.items():
            letters.append(letter.type)
        return letters

    def is_win(self):
        return self.letter_objects_to_list_of_letters(self.guessed_quote_letters) == \
               self.letter_objects_to_list_of_letters(
            self.decoded_quote_letters)

    def is_game_over(self):
        return '_' not in self.letter_objects_to_list_of_letters(self.guessed_quote_letters) and 'mistake' not \
               in self.letter_objects_to_list_of_letter_types(self.guessed_quote_letters)

    def calculate_time(self):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        return time.strftime("%M:%S", time.gmtime(total_time))

    def display_alphabet(self, quote):
        output = ""
        for key, value in quote.items():
            output += f'{key} '
        output += "\n"
        for key, value in quote.items():
            output += f'{value.letter} '
        return output

    def display_quote(self, quote):
        output = ""
        for key, value in quote.items():
            if value.type == "hint":
                output += Fore.MAGENTA + f'{value.letter} ' + Fore.RESET
            elif value.type == "mistake":
                output += Fore.RED + f'{value.letter} ' + Fore.RESET
            elif value.type == "guess":
                output += Fore.GREEN + f'{value.letter} ' + Fore.RESET
        return output

    def display_encoded_quote(self, quote):
        output = ""
        for key, value in quote.items():
            output += Fore.BLUE + f'{value.letter} ' + Fore.RESET
        return output

    def __str__(self):
        output = ""
        output += self.display_alphabet(self.alphabet) + "\n\n"
        output += self.__repr__()
        return output

    def __repr__(self):
        output = ""
        output += self.display_encoded_quote(self.encoded_quote_letters) + "\n"
        output += self.display_quote(self.guessed_quote_letters) + "\n"
        return output

    def __eq__(self, other):
        return self.letter_objects_to_list_of_letters(self.guessed_quote_letters) == \
               self.letter_objects_to_list_of_letters(other)
