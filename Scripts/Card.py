# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import collections
Card = collections.namedtuple('card', ['rank','suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._card = [card(rank,suit) for suit in suits
                      for rank in ranks]
        
    def __len__(self):
        return len(self._card)
    
    def __getitem__(self, position):
        return self._card[position]
        
        