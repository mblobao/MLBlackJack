from numpy.random import random
from decks import Player, Deck


class BJPlayer(Player):
    ''' BJPlayer - Black Jack player heritage from player
    Properties:
        cash
    Methods:
        __abs__: sum of the cards hand according to the rules
    '''
    def __init__(self, name, npc, dificulty='normal', cash=0):
        super().__init__(name=name, npc=npc, dificulty=dificulty)
        self.__cash = round(float(cash), 2)

    def __abs__(self):
        val, na = 0, 0
        for card in self.hand:
            if card.number.isnumeric():
                val += int(card.number)
            elif card.number in ['J', 'Q', 'K']:
                val += 10
            elif card.number == 'A':
                val += 11
                na += 1
        for i in range(na):
            if val > 21:
                val -= 10
        return val

    burn = property(fget=lambda self: abs(self) > 21)

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, value):
        self.__cash += value
        self.__cash = round(self.__cash, 2)


class BlackJack:
    """ BlackJackClass - Main actions for the game """
    class Mode:
        dark = 0
        one_up = 1
        dark_dealer = 2
        one_up_dealer = 3

    def __init__(self, names, players=2, mode=Mode.dark):
        self.__mode = mode
        if players < len(names):
            players = len(names) + 1
        self.players = [BJPlayer(name=nome, npc=False) for nome in names]
        for i in range(players - len(self.players)):
            self.players.append(BJPlayer(name=f'NPC-{i}', npc=True))
        if len(self.players) > 7:
            raise Exception("No more than 7 players, please...")
        if mode in [self.Mode.dark_dealer, self.Mode.one_up_dealer]:
            self.players.append(BJPlayer(name="Dealer", npc=True))
        self.deck = Deck()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            raise exc_val

    def start(self):
        # Initialize each player hand with 2 cards
        self.deck.shuffle()
        while sum(len(player) for player in self.players) < 2 * len(self.players):
            for player in self.players:
                player.get_card(self.deck.draw())
        for player in self.players:
            if player.name == 'Dealer' and player.is_npc:
                while abs(player) < 17:  # For dealer type games, dealer cannot start with less than 17 points
                    player.get_card(self.deck.draw())

    def roll(self):  # Play a round
        plays = sum(1 for player in self.players if not player.burn or not (player.name == 'Dealer' and player.is_npc))
        result = {'asks': 0, 'non-asks': 0, 'unknown': plays}  # plays counts the number of players in the roll
        while result['unknown'] > 0:
            for player in self.players:
                if player.name == 'Dealer' and player.is_npc:  # Dealers only draw cards in the game start

                if not player.burn:
                    if player.is_npc:
                        if round(random()) == 1:  # Modify with machine learning decision making in future version
                            result['asks'] += 1
                            result['unknown'] -= 1
                            player.get_card(self.deck.draw())
                        else:
                            result['non-asks'] += 1
                            result['unknown'] -= 1
                    else:
                        adver = {play.name: f"{len(play)} cards" for play in self.players}
                        ask = input(str(f"Opponent:\n"
                                        f"{adver}"
                                        f"Your cards {[card for card in player.hand]}\n"
                                        f"Draw a card? (y/n):\n"))
                        while ask.lower() not in ['y', 'n']:
                            ask = input("Sorry?!\nWanna draw a card? (y/n):\n")
                        if ask.lower() == 'y':
                            result['asks'] += 1
                            result['unknown'] -= 1
                            player.get_card(self.deck.draw())
                        else:  # if 'n'
                            result['non-asks'] += 1
                            result['unknown'] -= 1
                player.last_roll = result
            asks = result['asks']
        return result
