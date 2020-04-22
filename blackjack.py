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

test_deck = Deck()
print(test_deck)