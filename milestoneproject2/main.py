import random

values = {"Ace(1)":1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
          "Nine": 9, "Ten": 10, "Ace": 11, "Jack": 10, "Queen": 10, "King": 10}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace(1)","Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Ace", "Jack", "Queen", "King"]
dealer_names = ["DAN", "TEO", "SEBY", "PIS", "RARES", "DAVID", "ANDREI", "CIRJE"]


# CARD CLASS
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit} : {self.value}"


# PLAYER CLASS - attribute:balance,current_cards,name
class Player:
    def __init__(self, name, balance):
        self.balance = balance
        self.current_cards = []
        self.name = name

    def __str__(self):
        return f"Player {self.name} has {self.current_cards} and a balance of {self.balance}."

    def bet_win(self, bet):
        self.balance += bet

    def bet_lose(self, bet):
        self.balance -= bet


# DEALER CLASS
class Dealer:
    def __init__(self):
        self.current_cards = []
        self.name = dealer_names[random.randint(0, len(dealer_names) - 1)]

    def __str__(self):
        return f"Dealer {self.name} has {self.current_cards}."


# DECK CLASS - .shuffle .deal_card
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in range(1,14):

                created_card = Card(suit, ranks[rank])
                self.cards.append(created_card)
        pass

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()



# GAME LOGIC
print('Welcome to the game of blackjack!')
# Player info
name = input('What is your name? : ')
balance = input('What is your buy-in? : ')
player = Player(name, balance)
player.balance = int(player.balance)
# Dealer info
dealer = Dealer()
print(f'{dealer.name} will be your dealer today.')
dealer_names.remove(dealer.name)
# making the deck and shuffling the cards
game_on = True
round_on = True
round_count = 0
sp = 0
sd = 0
while game_on:

    ace = True
    ace_in_hand = False
    early_win = False
    game_on = True
    round_on = True

    round_count += 1
    # DEALER CHANGE
    if round_count-1 == 3:
        round_count = 0
        print('CHANGING DEALERS....')
        dealer.name = dealer_names[random.randint(0, len(dealer_names) - 1)]
        print(f'Your new dealer is {dealer.name}')
        dealer_names.remove(dealer.name)
        if dealer_names == []:
            print('All dealers have played. Adding them again....')
            dealer_names = ["DAN", "TEO", "SEBY", "PIS", "RARES", "DAVID", "ANDREI", "CIRJE"]

    # MAKING AND SHUFFLING DECK
    deck = Deck()
    deck.shuffle()

    # CHOOSING BET or closing game
    bet_notvalid = True
    while bet_notvalid:
        while True:
            try:
                bet = input('How much would you like to bet? (enter quit or exit to stop playing) : ')
                bet = int(bet)
                break
            except ValueError:
                if bet == 'quit' or bet == 'exit':
                    game_on = False
                    print('END OF BLACKJACK SESSION')
                    break


        if game_on == False:
            break

        if bet > player.balance:
            print('Sorry, you do not have enough money for chosen bet.')
        else:
            bet_notvalid = False
    if game_on == False:
        break


    # DEALING INITIAL CARDS
    #player.current_card = []
    #dealer.current_card = []
    player.current_cards.append(deck.deal_card())
    dealer.current_cards.append(deck.deal_card())
    player.current_cards.append(deck.deal_card())
    dealer.current_cards.append(deck.deal_card())

    # DISPLAYING INITIAL CARDS
    sp = 0
    for card in player.current_cards:
        sp += card.value
        if card.value == 11:
            ace_in_hand = True
    if ace_in_hand == True and ace == True and sp > 21:
        ace_index = 0
        for card in player.current_cards:
            if card.value == 11:
                player.current_cards.insert(ace_index, Card(card.suit, 'Ace(1)'))
                player.current_cards.remove(card)
                ace = False
                break
            ace_index += 1
    sp = 0
    print('YOUR CARDS:')
    for card in player.current_cards:
        print(card)
        sp += card.value
    print(f'Total: {sp}')
    sd = 0
    for card in dealer.current_cards:
        sd += card.value
    print("DEALER'S CARDS: ")
    print(dealer.current_cards[0])
    print('--hidden card--')
    print(f'Total: {dealer.current_cards[0].value} + ?')
    print('-----------------------------')


    # START OF PLAYER ACTIONS:
    while round_on:
        action = input('What do you want to do ? (hit,stand) : ')
        if action == 'stand':
            round_on = False
            sd = 0
            sp = 0
            print('YOUR CARDS:')
            for card in player.current_cards:
                print(card)
                sp += card.value
            print(f'Total: {sp}')
            print("DEALER'S CARDS: ")
            for card in dealer.current_cards:
                print(card)
                sd += card.value
            print(f'Dealer total: {sd}')
            print('-----------------------------')
            while sd < 17:
                dealer.current_cards.append(deck.deal_card())
                sd = 0
                sp = 0
                print('YOUR CARDS:')
                for card in player.current_cards:
                    print(card)
                    sp += card.value
                print(f'Total: {sp}')
                print("DEALER'S CARDS: ")
                for card in dealer.current_cards:
                    print(card)
                    sd += card.value
                print(f'Dealer total: {sd}')
                print('-----------------------------')
        elif action == 'hit':
            sp = 0
            sd = 0
            print('YOUR CARDS:')
            player.current_cards.append(deck.deal_card())
            for card in player.current_cards:
                sp += card.value
                if card.value == 11:
                    ace_in_hand = True
            if ace_in_hand == True and ace == True and sp > 21:
                ace_index = 0
                for card in player.current_cards:
                    if card.value == 11:
                        player.current_cards.insert(ace_index, Card(card.suit, 'Ace(1)'))
                        player.current_cards.remove(card)
                        ace = False
                        break
                    ace_index += 1
            sp = 0
            for card in player.current_cards:
                print(card)
                sp += card.value
            print(f'Total: {sp}')
            print("DEALER'S CARDS: ")
            print(dealer.current_cards[0])
            print('--hidden card--')
            print(f'Total: {dealer.current_cards[0].value} + ?')
            print('-----------------------------')

        sp = 0
        sd = 0
        for card in player.current_cards:
            sp += card.value
        for card in dealer.current_cards:
            sd += card.value
        if sp > 21:
            player.bet_lose(bet)
            round_on = False
            early_win = True
            print('BUST!')
        elif sp < 22 and sd > 21:
            player.bet_win(bet)
            round_on = False
            early_win = True
            print('DEALER BUSTED!')

    if early_win == False:
        sp = 0
        sd = 0
        for card in player.current_cards:
            sp += card.value

        for card in dealer.current_cards:
            sd += card.value

        if sp > sd:
            player.bet_win(bet)
            round_on = False
            print('YOU WON!')
        elif sp <= sd:
            player.bet_lose(bet)
            round_on = False
            print('DEALER WON!')
    print(f'Current balance: {player.balance}')
    player.current_cards.clear()
    dealer.current_cards.clear()

