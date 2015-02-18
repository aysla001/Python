# Coursera: Introduction to Interactive Programming
# Mini Project 6
# AY 20141101
# http://www.codeskulptor.org/#user38_m9Ui4qksna_31.py



import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.ahand=[]
        #pass	# create Hand object

    def __str__(self):
        hand_str = "Hand Contains: "
        for each in self.ahand:
            hand_str += "".join(str(each))
            hand_str += " "
        return hand_str
        #pass	# return a string representation of a hand

    def add_card(self, card):
        self = self.ahand.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        for each in self.ahand:
            hand_value += VALUES[each.rank]
        ## Do we have to loop twice to make sure we evaluate the hand at the end
        for each in self.ahand:
            if each.rank == 'A':
                if hand_value+10 <21:
                    hand_value += 10
        return hand_value
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        x = pos[0]
        y = pos[1]
        num = 1
        for each in self.ahand:
            each.draw(canvas,(x+num, y))
            num += 72
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.adeck =[]
        for x in SUITS:
            for y in RANKS:
                self.adeck.append(Card(x, y))
        pass	# create a Deck object

    def shuffle(self):
        random.shuffle(self.adeck)
        #pass    # use random.shuffle()

    def deal_card(self):
        l = len(self.adeck)
        x = self.adeck[l-1]
        self.adeck.pop(l-1)
        return x
        #pass	# deal a card object from the deck
    
    def __str__(self):
        deck_str = ""
        for each in self.adeck:
            deck_str += "".join(str(each))
            deck_str += " "
        return deck_str
       #pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play
    global d1, player_hand, dealer_hand
    if in_play== True:
        outcome = "Player Redelt! Dealer wins!"
        in_play = False
    else:
        in_play = True
    d1 = Deck()
    d1.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    #print d1
    player_hand.add_card(d1.deal_card())
    player_hand.add_card(d1.deal_card())
    dealer_hand.add_card(d1.deal_card())
    dealer_hand.add_card(d1.deal_card())
    #print "P1", (player_hand)
    #print "P1 value", (player_hand.get_value())
    #print "Dealer", (dealer_hand)
    #print "Dealer value", (dealer_hand.get_value())
    

def hit():
    global outcome, in_play
    player_hand.add_card(d1.deal_card())
    if player_hand.get_value() > 21:
        in_play = False
        outcome = "Player BUSTED! Dealer wins!"
        #print d1
        
def stand():
    global outcome, in_play
    while (dealer_hand.get_value()<17):
        dealer_hand.add_card(d1.deal_card())
    if dealer_hand.get_value() >21:
        outcome = "Player wins!"
        in_play = False
    elif player_hand.get_value() > dealer_hand.get_value():
        outcome = "Player wins!"
        in_play = False
    else:
        outcome = "Dealer wins!"
        in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [250, 20], 24, "White")
    canvas.draw_text("Players hand", [0, 60], 20, "Purple")
    canvas.draw_text("Dealers hand", [0, 185], 20, "Purple")
    player_hand.draw(canvas,[0,70])
    dealer_hand.draw(canvas,[0,200])
    if in_play == True:
        canvas.draw_image(card_back, [108,48], [72,96], [108,249] , [72,96])
        canvas.draw_text("Player move Hit or Stand?", [150, 45], 24, "Red")
    elif in_play == False:
        canvas.draw_text(outcome, [250, 45], 24, "Blue")



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

#c1 = Card("S", "A")
#hand1 = Hand()
#hand1.add_card(c1)
#print hand1
#print hand1.get_value()
#d1 = Deck()
#d1.shuffle()
#print d1
#print d1.deal_card()
#print d1

# remember to review the gradic rubric