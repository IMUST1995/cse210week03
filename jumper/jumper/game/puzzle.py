from ast import IsNot
import random

class Puzzle:
        def __init__(self):
            self.__listWords = ['lion', 'panther', 'cat', 'tiger']
            self.__word_selected = random.choice(self.__listWords)
            self.__word_guessing = [" _"] * len(self.__word_selected)

        def get_word__selected(self):
            return self.__word_selected

        def draw_word(self):
            print(f'\n{"".join(self.__word_guessing)}')
            
        #if letter guess is in the list continua el programa si no esta devuelve true para ejecutar method which remove a life to the jumper
        def update_draw_puzzle(self, letter):
            list_letters_word_selected = list(self.__word_selected)
            #replacing lettter guess in the draw
            if letter in list_letters_word_selected:
                self.__word_guessing[list_letters_word_selected.index(letter)] = letter
        def process_guess(self, letter):
            if letter in self.__word_selected:
                print(f'You guess a letter!')
                return False
            else:
                print(f'Wrong letter')
                return True

        #if _ sign is not in the list. return false and ends program
        def can_continue_guessing(self):
            if " _" in self.__word_guessing:
                return True
            else:
                print(f'You win!, the word is "{self.__word_selected}"')
                return False