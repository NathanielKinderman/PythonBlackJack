import random

#Global Variables
suits = ('Hearts','Spades','Diamonds','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3,'Four':4,'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
         
playing = True


class Card:
    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    #We need to start with an empty list
    #Nested for loops to itirate between the two tuples
    #Build Card objects and add to list
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    #start with an empty string
    def __str__(self):
        deck_comp= ''
        #add each Card object in print string
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The Deck has:' + deck_comp
    
    #using import random use shuffle()
    def shuffle(self):
        random.shuffle(self.deck)

    #function to deal one card from deck
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#class hand will equal player
class Hand:
    #will need attributes: card , value and aces(for the ace special rule)
    #self.card is wll need to be an empty list like deck
    #self.value will need to start at 0
    #self.aces will need to keep track of aces in deck
    def __init__(self):        
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    #I need the function to check if players value is greater than 21 and also minus an ace from the deck
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


#Keep track of how many chips to bet and player value
class Chips:

    #I set the default to 100 keep it consistent
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.totat -= self.bet

    
#I need a function to take input for bets and check if bet is greater the value of chips the player has
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips are you going to bet?: ')) 
        except ValueError:
            print('Please enter and integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips for that bet. You have {}".format(chips.total))
            else:
                break