# init file for BlackJack Game
from blackjack import BlackJack

if __name__ == '__main__':
    with BlackJack('Tiago', players=7, mode=BlackJack.Mode.one_up) as game:
        game.play()

        print('goodbye')