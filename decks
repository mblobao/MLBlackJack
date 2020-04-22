from numpy.random import shuffle


class Card:
    __suits = ['D', 'S', 'H', 'C']
    __numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, number, suit):
        if suit.upper() in self.__suits:
            self.__suit = suit
        else:
            raise ValueError('Unrecognized suit')
        if str(number).upper() in self.__numbers:
            self.__number = number
        else:
            raise ValueError('Unrecognized card number')

    def __repr__(self):
        return str(f"{self.__number}.{self.__suit}")

    suits = property(fget=lambda self: self.__suits)
    numbers = property(fget=lambda self: self.__numbers)


class Deck(Card):
    def __init__(self):
        super().__init__('A', 'D')
        self.__set = list()
        for n in self.suits:
            self.__set += list(Card(number=i, suit=n) for i in self.numbers)

    def __len__(self):
        return len(self.__set)
    
    def shuffle(self):
        self.__init__()
        shuffle(self.__set)

    def reset(self):
        self.__init__()
    
    def draw(self):
        card = self.__set[0]
        self.__set.pop(0)
        return card


class Jogador:
    def __init__(self, name, npc, dificulty='normal'):
        self.__name = str(name)
        self.__npc = bool(npc)
        self.__hand = list()
        self.__dificulty = dificulty

    def __len__(self):
        return len(self.__hand)

    hand = property(fget=lambda self: self.__hand)

    def get_card(self, card):
        self.__hand.append(card)

    def drop_card(self, card):
        if card not in self.__hand:
            raise Exception(f"Card not in {self.__name}'s hand")
        self.__hand.remove(card)
        return card

    def clear_hand(self):
        self.__hand = list()
