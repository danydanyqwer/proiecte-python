import random

# CARD
# SUIT,RANK,VALUE
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Ace': 11, 'Jack': 12, 'Queen': 13, 'King': 14}
suits = ('Hearts', 'Diamonds', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Jack', 'Queen', 'King')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + "of" + self.suit


# DECK
class Deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


# PLAYER
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# GAME SETUP
player_one = Player(name='one')
player_two = Player(name='two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_card())
    player_two.add_cards(new_deck.deal_card())

game_on = True
round_number = 0
while game_on:

    round_number += 1
    print(f'Round {round_number}')

    if len(player_one.all_cards) == 0:
        print(f'Player {player_one.name} has no cards. Player {player_two.name} wins!')
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print(f'Player {player_two.name} has no cards. Player {player_one.name} wins!')
        game_on = False
        break

    # START A NEW ROUND
    player_one_currentcards = []
    player_one_currentcards.append(player_one.remove_one_card())
    player_two_currentcards = []
    player_two_currentcards.append(player_two.remove_one_card())


    war_on = True
    while war_on:
        if player_one_currentcards[-1].value > player_two_currentcards[-1].value:
            player_one.add_cards(player_one_currentcards)
            player_one.add_cards(player_two_currentcards)
            war_on = False

        elif player_two_currentcards[-1].value > player_one_currentcards[-1].value:
            player_two.add_cards(player_one_currentcards)
            player_two.add_cards(player_two_currentcards)
            war_on = False

        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print(f'Player {player_one.name} unable to declare WAR')
                print(f'Player {player_two.name} wins!')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print(f'Player {player_two.name} unable to declare WAR')
                print(f'Player {player_one.name} wins!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_currentcards.append(player_one.remove_one_card())
                    player_two_currentcards.append(player_two.remove_one_card())