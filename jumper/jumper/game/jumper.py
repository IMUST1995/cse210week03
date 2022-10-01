import random

class Jumper:
    def __init__(self):
        self.__jumper_life = 4
    #method which will draw the jumper based in his lives
    def draw_jumper_life(self):
        jumper = "(-.-) Nap time."
        if  self.__jumper_life == 4:
            jumper = "  ___\n /___\\\n \\   /\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self.__jumper_life == 3:
            jumper = "\n /___\\\n \\   /\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self.__jumper_life == 2:
            jumper = "\n \\   /\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self.__jumper_life == 1:
            jumper = "\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self.__jumper_life <= 0:
            jumper = "\n   x\n  /|\\\n  / \\\n\n^^^^^^^"
        return jumper
    #method called when the letter is not in the word
    def remove_jumper_life(self):
            self.__jumper_life -= 1
    #method called to check the life of the jumper, if it returns 0 or less program ends.
    def return_life(self):
        return self.__jumper_life
    #def is_found(self):
        #return (self._distance[-1] == 0)
        
    #def watch_seeker(self, seeker):
        #distance = abs(self._location - seeker.get_location())
        #self._distance.append(distance)