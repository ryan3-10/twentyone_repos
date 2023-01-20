'''
Project: Twenty One Game:
Course:
Name: 
Due Date:

Description:
<put your description here>

This is skeleton starter code for the Twenty-One Game.

Typical pseudocode for such a game would be:
1. initial deal
2. player's turn 
3. If player gets twenty-one, immediate win 
4. dealer's turn 
5. check for winner
6. print results
'''

import os
import random

class Card:
    suit = ["Spades", "Clubs", "hearts", "Diamonds"]
    value = ["A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    numeric_value = [1, 11, 10, 2, 3, 4, 5, 6, 7, 8, 9]

    @staticmethod
    def show_cards():
        print(f"Player's Cards:")
        for card in Player.hand:
            sign = Deck.suits_values[card[1]]
            print(f"""
------------------        
|  {card[0]}             |
|                |
|                |
|                |
|                |
|       {sign}        |
|                |
|                |
|                |
|                |
|              {card[0]} |
|                |
------------------""")
        print(f"Player Score: {Hand.calculate_scores()[0]}")
        print("Dealer's Cards:")
        for card in Dealer.hand:
            sign = Deck.suits_values[card[1]]
            if card == Dealer.hand[0]:
                print(f"""
------------------        
|  {card[0]}             |
|                |
|                |
|                |
|                |
|       {sign}        |
|                |
|                |
|                |
|                |
|              {card[0]} |
|                |
------------------""")
            else:
                print("""
------------------        
|  ?             |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|              ? |
|                |
------------------""")
        print(f"Dealer's Score: {Hand.calculate_scores()[1]}")
                  
                        
    
    def __init__(self):
        pass
class Deck:
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    numeric_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    full_deck = []
    for suit in suits:
        for value in values:
            full_deck.append((value, suit))
    
    def __init__(self):
        pass

    @classmethod
    def shuffle(cls):
        random.shuffle(cls.full_deck)
    
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass
    
    @staticmethod
    def add(card, hand):
        if hand == "player":
            Player.hand.append(card)
        elif hand == "dealer":
            Dealer.hand.append(card)

    @staticmethod    
    def calculate_scores():
        player_score = 0
        dealer_score = 0 
        for card in Player.hand:
            player_score += Deck.numeric_values[card[0]]
        for card in Dealer.hand:
            dealer_score += Deck.numeric_values[card[0]]
        return (player_score, dealer_score)

class Dealer:
    hand = []
    deck = Deck
    
    def __init__(self):
        pass

    def deal(self):
        pass

class Player:
    hand = []
    def __init__(self):
        pass

class Game:

    def __init_(self):
        pass

    def run(self):
        pass
    
    @staticmethod
    def initial_deal():
        for _ in range(2):
            Hand.add(Deck.full_deck.pop(0), "player")
            Hand.add(Deck.full_deck.pop(0), "dealer")

    def player_turn(self):
        pass

    def dealer_turn(self):
        pass

    def check_winner(self):
        pass

    def results(self):
        pass

def clear():
   """Clear the console."""
   # for windows
   if os.name == 'nt':
      _ = os.system('cls')
   # for mac and linux, where os.name is 'posix'
   else:
      _ = os.system('clear')

def main():
    Deck.shuffle()
    Game.initial_deal()
    Card.show_cards()
    
    
    
    

if __name__ == '__main__':
    main()

