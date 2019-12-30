import random
import numpy as np
from math import *

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    """    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()
"""
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length - 1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


class Gamer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def currentplayer(self):
        print("Player1 is {}".format(self.name))
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card.show())
            else:
                return False
        return True

    def hidesecondecarte(self):
        print("{}'s hand: {}".format(self.name, self.hand[0]))
        return self

    # Display all the cards in the players hand
    def showHand(self):
        print("{}'s hand: {}".format(self.name, self.hand))

        return self

    def discard(self):
        return self.hand.pop()


    def somme(self):
        c = np.array([])
        for a in self.hand:
            #print(a[0:2])
            c = np.append(c, a[0:2])
        c = np.where(c == "Ki", 10, c)
        c = np.where(c == "Qu", 10, c)
        c = np.where(c == "Ja", 10, c)
        c = np.where(c == "Ac", 11, c)
        if np.sum([int(c[i]) for i in range(len(c))]) > 21:
            c = np.where(c == "11", 1, c)
        return np.sum([int(c[i]) for i in range(len(c))])
    def lost(self):
        if self.somme() > 21:
            return True
        else:return False


