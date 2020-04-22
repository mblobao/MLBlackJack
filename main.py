#init file for BlackJack Game
from blackjack import *

if __name__ == '__main__':
    game = BlackJack(['Тиаго','Marcelf'], 2)
    game.start()
    game.roll()