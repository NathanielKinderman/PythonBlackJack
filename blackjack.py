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
        self.total -= self.bet

    
#I need a function to take input for bets and check if bet is greater the value of chips the player has
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips are you going to bet?: \n')) 
        except ValueError:
            print('Please enter and integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips for that bet. You have {}".format(chips.total))
            else:
                break


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    #variable playing to control the game flow 
    global playing
    
    while True:
        choice = input(" Do you want to Hit or Stand? Enter 'h' or 's': ")
        
        #if player chooses to hit
        if choice[0].lower() == 'h':
            hit(deck,hand)
        
        #if player chooses to stand
        elif choice[0].lower() == 's':
            print("Player Stands. Now its the dealers turn")
            playing = False

        else:
            print('Please try again:')
            continue
        break

#function to show the players cards in a for loop and hides one of the dealers card
def show_some(player,dealer):
    print('DEALERS HAND:')
    print('one card is hidden')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    
    for card in player.cards:
        print(card)

#function to show all cards when the game is over
def show_all(player,dealer):
    print("'DEALERS HAND:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)

#show when player bust
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

#show when player wins
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

#show when dealer busts
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

#show when dealer wins   
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

#show when theres a tie   
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

#actual game play flow:
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break