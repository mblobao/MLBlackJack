from colorama import Fore, Back, Style # colored printing for default console
from curses import wrapper # ncurses module

import sys
import os

class Console:
    """ Console class
    Manages console printing
    Properties:
        screen: stdscr object from curses
        mode: type of printing
            - CURSES_MODE
            - DEFAULT_MODE
    Methods:
        print - print on console accordingly to selected mode        
        clear - clear screen using provided resources to do it
    """

    ''' ----------------- STATIC ATRIBUTES ----------------- '''
    # constants
    class mode:
        CURSES_MODE = 0
        DEFAULT_MODE = 1

    class character:
        ENTER_CHAR = '\n'
        SPACE_CHAR = ' '

    textColor = Fore
    style = Style

    # stolen function from cruses
    wrapper = wrapper

    ''' ----------------- PRIVATE ATRIBUTES ----------------- '''
    # outputBuffer

    # Mode Getters
    def __isCursesMode__(self):
        return True if self.__mode == self.mode.CURSES_MODE else False
    def __isDefaultMode__(self):
        return True if self.__mode == self.mode.DEFAULT_MODE else False

    ''' ----------------- PUBLIC ATRIBUTES ----------------- '''
    def __init__(self,mode):
        self.__mode = mode
        try:
            self.__columns, self.__rows = os.get_terminal_size(0)
        except OSError:
            self.__columns, self.__rows = os.get_terminal_size(1)

    def print(self,inputString,color=Style.RESET_ALL):
        if self.__isCursesMode__():
            pass
        if self.__isDefaultMode__():
            sys.stdout.write(color)
            sys.stdout.write(str(inputString))
            sys.stdout.write(Style.RESET_ALL)


    
    def clear(self):
        if self.__isCursesMode__():
            pass
        if self.__isDefaultMode__():
            returns = ''
            # pylint: disable=unused-variable
            for i in range(self.__columns):
                returns += self.character.ENTER_CHAR
            print(returns)




