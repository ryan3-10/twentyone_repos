'''
Project: Twenty One Game:
Course: CS1410 X01
Name: Ryan Coutts
Due Date: 01/20/2023

Description:
Program plays a game of twenty-one against a programmed dealer. After the initial deal of
2 cards, the player chooses to either take another hit, or stand. Player may continue to 
take an additional card until he reaches a score of 21 or higher. Reaching exactly 21 means
the player automatically wins. Going over 21 means the player automatically loses. 
Note: this program is best ran on a vertical terminal... '''

import os
import random

class Card:
    suit = ["Spades", "Clubs", "hearts", "Diamonds"]
    value = ["A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    numeric_value = [1, 11, 10, 2, 3, 4, 5, 6, 7, 8, 9]
    def __init__(self):
        pass
    
    @staticmethod
    def show_cards(face_down):
        '''Prints the cards and scores.'''
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
        print(f"Player's Score: {Hand.calculate_scores()[0]}")
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
                if face_down == True:
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
                elif face_down == False:
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
        if face_down == True:
            print(f"Dealer's Score: {Deck.numeric_values[Dealer.hand[0][0]]}")
        elif face_down == False:
            print(f"Dealer's Score: {Hand.calculate_scores()[1]}")
        
class Deck:
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    numeric_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    full_deck = []
    for suit in suits:
        for value in values:
            full_deck.append((value, suit))
    #Appends all 52 cards into one list.
    
    def __init__(self):
        pass

    @classmethod
    def shuffle(cls):
        '''Randomizes the order of the full deck list.'''
        random.shuffle(cls.full_deck)

class Hand:
    def __init__(self):
        pass
    
    @staticmethod
    def add(card, hand):
        '''Adds a card to either the player or dealer's hand.'''
        if hand == "player":
            Player.hand.append(card)
        elif hand == "dealer":
            Dealer.hand.append(card)

    @staticmethod    
    def calculate_scores():
        '''Calculates and returns the scores of the player and dealer.'''
        player_score = 0
        dealer_score = 0 
        for card in Player.hand:
            if card[0] == 'A' and player_score > 10:
                player_score += 1
            else:
                player_score += Deck.numeric_values[card[0]]
        for card in Dealer.hand:
            if card[0] == 'A' and dealer_score > 10:
                dealer_score += 1
            else:
                dealer_score += Deck.numeric_values[card[0]]
        return (player_score, dealer_score)

class Dealer:
    hand = []
    deck = Deck
    
    def __init__(self):
        pass

class Player:
    hand = []

    def __init__(self):
        pass

class Game:
    def __init_(self):
        pass

    def run(self):
        '''Runs all methods required for the game.'''
        self.initial_deal()
        self.dealer_turn(self.player_turn(Deck.full_deck))
        self.results(self.check_winner())
    
    @staticmethod
    def initial_deal():
        '''Deals 2 cards to both the player and the dealer.'''
        for _ in range(2):
            Hand.add(Deck.full_deck.pop(0), "player")
            Hand.add(Deck.full_deck.pop(0), "dealer")

    def player_turn(self, full_deck):
        '''The player choses to hit or stand.'''
        player_stands = False
        while Hand.calculate_scores()[0] < 21 and player_stands == False:
            Card.show_cards(True)
            answer = input("Player's turn\nInput '1' to hit\ninput '2' to stand\n>")
            if answer == '1':
                Hand.add(full_deck.pop(0), "player")
            elif answer == '2':
                player_stands = True
            else:
                print("Invalid input")
        return full_deck

    def dealer_turn(self, full_deck):
        '''The dealer hits until he reaches a score of 17 or higher.'''
        while Hand.calculate_scores()[1] < 17:
            Hand.add(full_deck.pop(0), "dealer")
        Card.show_cards(False)
        

    def check_winner(self):
        '''Determines who won and which situation it was.'''
        pscore = Hand.calculate_scores()[0]
        dscore = Hand.calculate_scores()[1]
        if pscore > 21:
            verdict = "player bust"
        elif dscore > 21:
            verdict = "dealer bust"
        elif pscore == 21:
            verdict = "player 21"
        elif pscore == dscore:
            verdict = "tie game"
        elif pscore > dscore:
            verdict = "player closest"
        elif dscore > pscore:
            verdict = "dealer closest"
        return verdict
        
    def results(self, verdict):
        '''Prints the final results of the game.'''
        pscore = Hand.calculate_scores()[0]
        dscore = Hand.calculate_scores()[1]
        possible_results = {"player bust": "You busted. Dealer wins!", "dealer bust": "Dealer busted. You win!",
        "player 21": "You hit 21 exactly! You win!", "tie game": "You and the dealer have the same score. Tie game!",
        "player closest": "Your score is closer to 21. You win!", "dealer closest": "Dealer is closesr to 21. Dealer wins!"}
        print(f"Final Scores:\nPlayer: {pscore}\nDealer: {dscore}\n{possible_results[verdict]}") 

def clear():
   """Clear the console."""
   # for windows
   if os.name == 'nt':
      _ = os.system('cls')
   # for mac and linux, where os.name is 'posix'
   else:
      _ = os.system('clear')

def main():
    '''Shuffles the deck and then runs the game.'''
    my_play = Game()
    Deck.shuffle()
    my_play.run()

if __name__ == '__main__':
    main()

