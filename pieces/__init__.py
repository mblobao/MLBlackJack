from typing import List
from MLBlackJack.pieces.dices import Dice, DiceGroup
from MLBlackJack.pieces.cards import Deck, Card


class Player:
    """ Player class
    Properties:
        get_card: list of cards
    Methods:
        get_card: add card to players hand
        drop_card: remove card from players hand
        clear_hand: removes all cards from players hand
    """
    def __init__(self, name: str):
        self.__name = name
        self.__hand: List[Card] = list()
    
    def get_card(self, card: Card)
    
    
    
