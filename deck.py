import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"] # clubs, diamonds, hearts, spades
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__() # repr is the same as str

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self.suit

class Deck:
    def __init__(self):
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop(0)

if __name__ == "__main__":
    c1 = Card("A","♣")
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())