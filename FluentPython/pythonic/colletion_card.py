#!/usr/bin/env python3
# coding=utf-8
# title          : colletion_card.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 3/25/19 9:07 PM
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(deck[0], deck[1], deck[-1], len(deck))
print("Random deck use choice:", choice(deck))
print("Slicing:", deck[:3])

# Iteration
for card in reversed(deck):
    print(card)

# Sorted
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]


print("SORTED======================================SORTED")
for card in sorted(deck, key=spades_high):
    print(card)
