from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
   
    def __init__(self):
        #first two to control the program execution
        self.__continuar = True
        self.__still_alive = True
        self.__puzzle = Puzzle()
        self.__jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        #if both conditions are true, the program will be execute
        while self.__still_alive and self.__continuar:
            #hold a letter tu update the life of jumper
            letter = self._get_inputs()
            self._do_updates(letter)
            self._do_outputs()
#
    def _get_inputs(self):
        """ self.__puzzle.update_draw_puzzle("i") """
        self.__puzzle.draw_word()
        #holding a jumper draw to print with the terminaal service.
        jumper_draw = self.__jumper.draw_jumper_life()
        self._terminal_service.print_jumper(jumper_draw)
        #holding the input letter
        new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        #hold a boolean true if the letter is in the words a false if not.
        return new_letter
        #self.__puzzle.move_location(new_location)
    def _do_updates(self, letter):
        #self._hider.watch_seeker(self._seeker)
        proccess_guess = self.__puzzle.process_guess(letter)
        if proccess_guess:
            self.__jumper.remove_jumper_life()
        #if the letter match will update the list of the draw    
        else:
            self.__puzzle.update_draw_puzzle(letter)
    def _do_outputs(self):
        #hint = self._hider.get_hint()
        #self._terminal_service.write_text(hint)
        #if self._hider.is_found():
            #self._is_playing = False
        self.__continuar = self.__puzzle.can_continue_guessing()
        #created variable to hold boolean from lives whre if higher than 0 return True and skip the conditional, if life is false (lower than 0), still alive become false, and ends program
        life = self.__jumper.return_life() > 0
        if not life:
            self.__still_alive = False
            jumper_draw = self.__jumper.draw_jumper_life()
            self._terminal_service.print_jumper(jumper_draw)
            print(f'End, the jumper is not longer available. =(')