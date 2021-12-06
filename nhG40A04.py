import QuoteManager
import CryptogramGameLogic
import Exceptions
from colorama import init, Fore, Back, Style
init()


def print_error_message(e):
    print(Fore.RED + f'{e} \n' + Fore.RESET)


def display_quote(quote):
    for letter, value in quote.items():
        print(Fore.BLUE + f'{value}', end=' ' + Fore.RESET)
    print()


def display_guessed_quote(quote):
    for letter, value in quote.items():
        print(Fore.GREEN + f'{value}', end=' ' + Fore.RESET)
    print()


def print_alphabet(alphabet):
    print("Alphabet")
    for letter, value in alphabet.items():
        print(f'{letter}', end=' ')
    print()
    for letter, value in alphabet.items():
        print(f'{value}', end=' ')
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
        if game_obj.can_receive_hint():
            game_obj.receive_hint()
        else:
            raise Exceptions.CantReceiveHintException()
    elif guess_input == "":
        raise Exceptions.EmptyGuessException()
    else:
        game_obj.determine_guess(guess_input)


def get_random_quote():
    quote_chosen = quote_manager.random_quote()
    start_game(quote_chosen)


def won(game_obj):
    answer = input("You won! Do you want to play again? (yes/no)")
    if answer.lower() == 'yes':
        get_random_quote()
    if answer.lower() == 'no':
        print("Bye!")
        exit(0)


def lost(game_obj):
    answer = input('Sorry, you lost. Do you want to play again or find all mistakes? Enter "play again" to '
                   'play again or "!" to find all mistakes.')
    if answer.lower() == 'play again':
        get_random_quote()
    if answer == '!':
        pass


def game_over(game_obj):
    print('game over')
    if game_obj.is_win():
        won(game_obj)
    else:
        lost(game_obj)


def start_game(_quote_chosen):
    game = CryptogramGameLogic.CryptogramGameLogic(_quote_chosen.quote)
    game.encode_quote()
    game.initialize_quote_dictionaries()
    game.initialize_decoded_dictionary()
    game.create_alphabet_dictionary()
    display_instructions()
    print(_quote_chosen.quote)
    while not game.is_game_over():
        try:
            print_alphabet(game.alphabet)
            display_quote(game.encoded_quote_letters)
            display_guessed_quote(game.guessed_quote_letters)
            guess = input(">>>")
            check_input(guess, game)
        except ValueError:
            print_error_message("Please enter a valid command")
        except Exceptions.EmptyGuessException as e:
            print_error_message(e)
        except Exceptions.EntryToLongException as e:
            print_error_message(e)
        except Exceptions.EntryTooShortException as e:
            print_error_message(e)
        except Exceptions.FirstLetterNotALetterException as e:
            print_error_message(e)
        except Exceptions.NoSpaceInBetweenConversionException as e:
            print_error_message(e)
        except Exceptions.SecondLetterNotALetterException as e:
            print_error_message(e)
        except Exceptions.CantReceiveHintException as e:
            print_error_message(e)
    else:
        display_quote(game.encoded_quote_letters)
        display_guessed_quote(game.guessed_quote_letters)
        game_over(game)


if __name__ == "__main__":
    print("Welcome to the cryptogram game")

    quote_manager = QuoteManager.QuoteManager()
    quote_manager.parse_url()
    quote_manager.create_quotes_dictionary()
    get_random_quote()
