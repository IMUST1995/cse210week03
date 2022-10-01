from ast import IsNot
import random

class Puzzle:
        def __init__(self):
            self.__listWords = ['buffalo', 'giraffe', 'elephant', 'lion']
            self.__word_selected = random.choice(self.__listWords)
            self.__word_guessing = ["_"] * len(self.__word_selected)

        def get_word__selected(self):
            return self.__word_selected

        def draw_word(self):
            print(self.__word_guessing)
            pass
        #if letter guess is in the list continua el programa si no esta devuelve true para ejecutar method which remove a life to the jumper
        def process_guess(self, letter):
            if letter in self.__word_selected:
                print(f'You guess a letter!')
                return False
            else:
                print(f'Wrong letter')
                return True

        #if _ sign is not in the list. return false and ends program
        def can_continue_guessing(self):
            if "_" in self.__word_guessing:
                return True
            else:
                return False