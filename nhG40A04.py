import QuoteManager
import CryptogramGameLogic
import Exceptions
from yachalk import chalk


def display_quote(quote):
    for letter, value in quote.items():
        print(f'{value}', end='')
    print()


def print_alphabet(_quote_chosen):
    print("Alphabet")
    print(*_quote_chosen.uppercase_ascii_letters, end=' ')
    print()
    print()


def display_instructions():
    print('''To convert a encoded letter you simply enter in:
"Any decoded letter" a space "Letter to replace"
Example: V A''')
    print()
    print()


def check_input(guess_input, game_obj):
    if guess_input == '!':
        game_obj.find_all_mistakes()
    elif guess_input == "?":
        game_obj.get_hint()
    elif guess_input == "":
        raise Exceptions.EmptyGuessException()
    else:
        game_obj.determine_guess(guess_input)


def start_game(_quote_chosen):
    game = CryptogramGameLogic.CryptogramGameLogic(quote_chosen)
    display_instructions()
    while not game.is_win():
        try:
            print_alphabet(_quote_chosen)
            display_quote(_quote_chosen.encoded_quote_letters)
            display_quote(_quote_chosen.guessed_quote_letters)
            guess = input(">>>")
            check_input(guess, game)
        except ValueError:
            print("Please enter a valid command")
        except Exceptions.EmptyGuessException as e:
            print(f'{e} \n')
        except Exceptions.EntryToLongException as e:
            print(f'{e} \n')
        except Exceptions.EntryTooShortException as e:
            print(f'{e} \n')
        except Exceptions.FirstLetterNotALetterException as e:
            print(f'{e} \n')
        except Exceptions.NoSpaceInBetweenConversionException as e:
            print(f'{e} \n')
        except Exceptions.SecondLetterNotALetterException as e:
            print(f'{e} \n')


if __name__ == "__main__":
    print("Welcome to the cryptogram game")

    quote_manager = QuoteManager.QuoteManager()
    quote_manager.parse_url()
    quote_manager.create_quotes_dictionary()

    quote_chosen = quote_manager.random_quote()
    quote_chosen.initialize_quote_dictionaries()
    quote_chosen.initialize_decoded_dictionary()

    start_game(quote_chosen)
