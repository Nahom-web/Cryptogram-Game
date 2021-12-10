# by Nahom Haile
# Advanced Topics in Computer Science I
# nhG40A04.py
# This file includes the CLI for the cryptogram game

import QuoteManager
import CryptogramGameLogic
import Exceptions
from colorama import init, Fore
init()


def print_error_message(e):
    print(Fore.RED + f'{e} \n' + Fore.RESET)


def display_instructions():
    print('''To convert a encoded letter you simply enter in:
"Any decoded letter" a space "Letter to replace"
Example "V A"

To receive a hint enter: ? (shown in purple)
To find all of your mistakes enter: ! (shown in red)
To end the game at any time enter: stop
To set any encoded letter back to an underscore, simply set it back to "_" following the input format.
''')


def check_input(guess_input, game_obj):
    if guess_input == '!':
        print("Finding all mistakes...")
        game_obj.find_all_mistakes()
    elif guess_input == "?":
        game_obj.can_receive_hint()
    elif guess_input == "stop":
        print('Thanks for playing!')
        exit(0)
    elif guess_input == "":
        raise Exceptions.EmptyGuessException()
    else:
        game_obj.determine_guess(guess_input)


def won(game_obj):
    game_obj.calculate_time()
    print(f'It took you: {game_obj.calculate_time()} minutes')
    print("You won! Do you want to play again? (yes/no)")
    answer = input(">>>")
    if answer.lower() == 'yes':
        get_random_quote()
    if answer.lower() == 'no':
        print("Bye!")
        exit(0)


def lost(game_obj):
    print('Sorry, you lost. Do you want to play a new game or find all the mistakes? Enter "play again" or "!" to '
          'remove all mistakes.')
    answer = input(">>>")
    if answer.lower() == 'play again':
        get_random_quote()
    if answer == '!':
        game_obj.remove_all_mistakes()
        start_game(game_obj)


def game_over(game_obj):
    print('game over')
    won(game_obj) if game_obj.__eq__(game_obj.decoded_quote_letters) else lost(game_obj)


def get_random_quote():
    quote_chosen = quote_manager.random_quote()
    set_up_game(quote_chosen)


def set_up_game(_quote_chosen):
    game = CryptogramGameLogic.CryptogramGameLogic(_quote_chosen.quote)
    game.encode_quote()
    game.initialize_quote_dictionaries()
    game.initialize_decoded_dictionary_of_quote_letters()
    game.create_alphabet_dictionary()
    display_instructions()
    start_game(game)


def start_game(game_obj):
    print(game_obj.quote_chosen)
    while not game_obj.is_game_over():
        try:
            print(game_obj.__str__())
            guess = input(">>>")
            check_input(guess, game_obj)
        except ValueError:
            print_error_message("Please enter a valid command")
        except Exceptions.NoSpaceInBetweenLettersException as e:
            print_error_message(e)
        except Exceptions.EmptyGuessException as e:
            print_error_message(e)
        except Exceptions.EntryToLongException as e:
            print_error_message(e)
        except Exceptions.EntryTooShortException as e:
            print_error_message(e)
        except Exceptions.FirstLetterNotALetterException as e:
            print_error_message(e)
        except Exceptions.SecondLetterNotALetterException as e:
            print_error_message(e)
        except Exceptions.CantReceiveHintException as e:
            print_error_message(e)
        except Exceptions.EncodedLetterIsNotInQuoteException as e:
            print_error_message(e)
    else:
        game_obj.find_all_mistakes()
        print(game_obj.__repr__())
        game_over(game_obj)


if __name__ == "__main__":
    print("Welcome to the cryptogram game")
    quote_manager = QuoteManager.QuoteManager()
    quote_manager.parse_url()
    quote_manager.create_quotes_dictionary()
    get_random_quote()
