import random

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
          "Nine": 9, "Ten": 10, "Ace": 11, "Jack": 10, "Queen": 10, "King": 10}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Ace", "Jack", "Queen", "King"]


# CARD CLASS
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit} : {self.value}"


# PLAYER CLASS - atribute:balance,current_cards,name
class Player:
    def __init__(self, balance, name):
        self.balance = balance
        self.current_cards = []
        self.name = name

    def __str__(self):
        return f"Player {self.name} has {self.current_cards} and a balance of {self.balance} "

    def bet(self, bet):
        pass
        # if bet > self.balance:
            # print(f"Sorry, you don't have enough funds for chosen bet.")


# DEALER CLASS


# DECK CLASS - .shuffle .deal_card
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.cards.append(created_card)
        pass

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
# TABLE CLASS


# GAME LOGIC
deck = Deck()

for x in deck.cards:
    print(x)
