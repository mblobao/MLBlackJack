# init file for BlackJack Game
from MLBlackJack.blackjack import BlackJack

if __name__ == '__main__':
    game = BlackJack(
        names=['Тиаго', 'Marcelf'],
        players=3
    )
    game.start()
    game.roll()