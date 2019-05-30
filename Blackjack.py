import random
suits = ["Hearts","Spades","Clubs","Diamonds"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
value = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
playing = True

class Card:
    def __init__(self,suit,rank):
        self.sum = 0
        self.suits = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(self.rank,self.suits)
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return  "The deck contains: " + deck_comp
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + value[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    def adjust_for_ace(self):
        if self.value >=10:
            self.value += 11
        else:
            self.value += 1
class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter How Much You'd Like to Bet"))
        except:
            print ("Sorry that was not an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry You cant bet more than you own")
            else:
                break
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
"""
while True:
    print("Welcome to BlackJack, You will be competing against the computer, the deck will now shuffle")
    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    player1.add_card(deck.deal())
    player1.add_card(deck.deal())
    dealer1 = Hand()
    dealer1.add_card(deck.deal())
    dealer1.add_card(deck.deal())
    player_chips = Chips()
    take_bet(player_chips)
    show_some(player1,dealer1)
    while playing:
        hit_or_stand(deck,player1)
        show_some(player1,dealer1)
        if player1.value > 21:
            player_busts(player1,dealer1,player_chips)
            break
    if player1.value <= 21:
        while dealer1.value < 17:
            hit(deck,dealer1)
        show_all(player1,dealer1)

        if player1.value > 21:
            player_busts(player1,dealer1,player_chips)
        elif dealer1.value > player.value:
            dealer_wins(player1,dealer1,player_chips)
        elif dealer1.value < player1.value:
            player_wins(player1,dealer1,player_chips)
        else:
            push(player1,dealer1)
    print("You're current total is " + str(player1.value))
"""
