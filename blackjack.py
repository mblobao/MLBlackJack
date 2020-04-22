from numpy import inf
from numpy.random import shuffle, random


class Carta:
    __naipes = ['O', 'E', 'C', 'P']
    __numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, numero, naipe,):
        if naipe.upper() in self.__naipes:
            self.naipe = naipe
        else:
            raise ValueError('Naipe não reconhecido')
        if str(numero).upper() in self.__numeros:
            self.numero = numero
        else:
            raise ValueError('Numero de carta não reconhecido')

    def __repr__(self):
        return str(f"{self.numero}.{self.naipe}")

    @property
    def valor(self):
        return self.numero if type(self.numero) is int else 10 if self.numero in ['J', 'Q', 'K'] else 11


class Baralho:
    def __init__(self):
        self.deck = list()
        for n in ['O', 'E', 'C', 'P']:
            self.deck += list(Carta(numero=i, naipe=n) for i in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
        self.deck = list(self.deck)

    def embararalhar(self):
        self.__init__()
        shuffle(self.deck)

    def draw(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card


class Jogador:
    def __init__(self, nome, npc, dificuldade='easy'):
        self.nome = nome
        self.npc = bool(npc)
        self.cartas = list()
        self.dificuldade = dificuldade
        self.last_roll = {'asks': 0, 'non-asks': 0, 'unknown': 0}

    def __len__(self):
        return len(self.cartas)

    @property
    def deck(self):
        main = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
        for card in self.cartas:
            main[str(card.numero).upper()] += 1
        return main

    @property
    def burn(self):
        return abs(self) > 21

    @property
    def result(self):
        if abs(self) == 21:
            return 2
        if abs(self) < 21:
            return 1
        else:
            return 0

    def __abs__(self):
        soma = sum(carta.valor for carta in self.cartas)
        as_ = 0
        for carta in self.cartas:
            if carta.numero == 'A':
                as_ += 1
        for i in range(as_):
            if soma > 21:
                soma = soma - 10
        return soma

    def receber(self, carta):
        self.cartas.append(carta)


class Rodada:
    def __init__(self, *nomes, players=2):
        if players < len(nomes):
            players = len(nomes) + 1
        self.players = [Jogador(nome=nome, npc=False) for nome in nomes]
        for i in range(players - len(self.players)):
            self.players.append(Jogador(nome=f'JungKook{i}', npc=True))
        if len(self.players) > 7:
            raise Exception("Não pode ter mais de 7 jogadores")
        self.deck = Baralho()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            raise exc_val

    def start(self):
        self.deck.embararalhar()
        while sum(len(player) for player in self.players) < 2 * len(self.players):
            for player in self.players:
                player.receber(self.deck.draw())

    def roll(self):
        play = sum(1 for player in self.players if not player.burn)
        result = {'asks': 0, 'non-asks': 0, 'unknown': play}
        asks = play
        while asks > 0:
            play = sum(1 for player in self.players if not player.burn)

            result = {'asks': 0, 'non-asks': 0, 'unknown': play}
            for player in self.players:
                if not player.burn:
                    if player.npc:
                        if round(random()) == 1:
                            result['asks'] += 1
                            result['unknown'] -= 1
                            player.receber(self.deck.draw())
                        else:
                            result['non-asks'] += 1
                            result['unknown'] -= 1
                    else:
                        adver = {play.nome: f"{len(play)} cartas" for play in self.players}
                        ask = input(str(f"Adversários:\n"
                                        f"{adver}"
                                        f"Suas cartas {[card for card in player.cartas]}\n"
                                        f"Deseja puxar uma carta? (s/n):\n"))
                        while ask.lower() not in ['s', 'n']:
                            ask = input("Não entendi!\nDeseja puxar uma carta? (s/n):\n")
                        if ask.lower() == 's':
                            result['asks'] += 1
                            result['unknown'] -= 1
                            player.receber(self.deck.draw())
                        else:
                            result['non-asks'] += 1
                            result['unknown'] -= 1
                player.last_roll = result
            asks = result['asks']
        return result


if __name__ == '__main__':
    with Rodada('Ester') as rod:
        rod.roll()
