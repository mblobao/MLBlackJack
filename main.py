#init class for handling output
from consoleGui import Console

# init file for BlackJack Game
from blackjack import BlackJack

if __name__ == '__main__':
    console = Console(mode=Console.mode.DEFAULT_MODE)
    
    # TO DO : Show Menu options for player and mode inputs

    with BlackJack('Tiago', players=7, console=console, mode=BlackJack.Mode.one_up) as game:
        game.play()

    console.print("Goodbye!")