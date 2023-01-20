import pytest
from twentyone import Card, Deck

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
numeric_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

def test_card():
   card = Card(suits_values["Hearts"], "A", numeric_values["A"])
   assert card.suit == suits_values["Hearts"]
   assert card.value == "A"
   assert card.numeric_value == numeric_values["A"]

   target = """----------------
|                |
|  A             |
|                |
|                |
|                |
|                |
|       \u2661        |
|                |
|                |
|                |
|                |
|             A  |
|                |
----------------"""

   assert str(card) == target

def test_deck():
   deck = Deck()
   assert not deck.is_empty()
   card = deck.hit()
   assert card.suit == suits_values["Diamonds"]
   assert card.value == "K"
   assert card.numeric_value == numeric_values["K"]

