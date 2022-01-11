import random



# Sets of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}




# Card object
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit




# Deck object
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card




# Hand object
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 




# Chips object
class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet




# Ask for bet
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('\nHow many chips would you like to bet?: '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break




# Get another card
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()




# Ask for hit or stand
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("\nWould you like to Hit or Stand? (Hit or Stand): ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("\nPlayer stands, Dealer is playing")
            playing = False

        else:
            print("Sorry, please try again")
            continue
        break




# Show Player's cards and half of Dealer's cards
def show_some(player,dealer):
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])




# Show Player's and Dealer's cards and values
def show_all(player,dealer):
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)




# Win conditions
def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("\nDealer and Player tie! It's a push")




# Ask for playing again
def play_again():
    while True:
        play_again = input("\nDo you want to play again? (Yes or No): ")
        if play_again[0].lower() == "y":
            return True
        if play_again[0].lower() == "n":
            return False
        else:
            print("That is not Yes or No, try again")








'''
GAME SETUP
'''



# Set up the Player's chips
player_chips = Chips()

while True:

    playing = True

    # Game explanation
    print('\nWelcome to BlackJack! Get as close to 21 as you can without going over! \nDealer hits until he reaches 17. Aces count as 1 or 11.')
    
    # Create the deck
    deck = Deck()
    deck.shuffle()
    
    # Give cards to the Player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    # # Give cards to the Dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    
    # Ask the Player to place his bet
    take_bet(player_chips)
    
    # Player's turn
    while playing:
        
        # Show the Player's cards
        show_some(player_hand,dealer_hand)
        
        # Ask the Player to hit or stand
        hit_or_stand(deck,player_hand)
        
        # Check if player busts
        if player_hand.value > 21:
            show_all(player_hand,dealer_hand)
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # Dealers turn after Player stands
    if player_hand.value <= 21:
        
        # Dealer checks if to hit or not
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

            # Show Player's and Dealer's cards
            show_all(player_hand,dealer_hand)

            # Try win conditions
            if player_hand.value == dealer_hand.value:
                push(player_hand,dealer_hand)
                break

            elif player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break

            elif dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
                break

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
                break
                
        else:

            while True:

                 # Show all cards
                show_all(player_hand,dealer_hand)

                # Try win conditions
                if player_hand.value == dealer_hand.value:
                    push(player_hand,dealer_hand)
                    break

                elif player_hand.value > 21:
                    player_busts(player_hand,dealer_hand,player_chips)
                    break

                elif dealer_hand.value > 21:
                    dealer_busts(player_hand,dealer_hand,player_chips)
                    break

                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand,dealer_hand,player_chips)
                    break

        
    # Tell the Player how many chips he has 
    print(f"\nYou now have {player_chips.total} chips")
    
    # Ask to play again
    if play_again():
        continue
    else:
        print("Thank you for playing")
        break
