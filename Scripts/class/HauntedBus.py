# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:52:14 2018

@author: hand
"""
class HauntedBus:class HauntedBus:
    '''备受幽灵折磨的校车'''
    
def __init__(self,passengers= []):
    self.passengers = passengers
    
def pick(self, name):
    self.passengers.append(name)
    
def drop(self, name):
    self.passengers.remove(name)
    
