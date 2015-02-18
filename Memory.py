# Coursera: Introduction to Interactive Programming
# Mini Project 5
# AY 20141025
# http://www.codeskulptor.org/#user38_ao5ySmgBgC_11.py

import simplegui
import random

global turns
turns = 0

# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global state
    state = 0
    exposed=[False,False, False, False,False, False, False, False, False, False, False, False,False,False,False,False] 
    deck1 = range(0,8)
    deck2 = range(0,8)
    deck = deck1 + deck2
    random.shuffle(deck) 

     
# define event handlers
def mouseclick(pos):
    global state
    global state1_value
    global state2_value
    global state1_sel
    global state2_sel
    global turns
    # add game state logic here
    card_sel = pos[0]/50
    sel= deck[card_sel]
    if state == 0:
        state = 1
        state1_sel = card_sel
        state1_value = deck[card_sel]
        exposed[state1_sel]=True
    elif state == 1:
        turns +=1 
        state = 2
        state2_value = deck[card_sel]
        state2_sel= card_sel
        exposed[state2_sel]=True
    else:
        state = 0
        if state1_value == state2_value:
            exposed[state1_sel]=True
            exposed[state2_sel]=True
        else:
            exposed[state1_sel]=False
            exposed[state2_sel]=False
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for x in range(0,16):
        if exposed[x] == False:
            #canvas.draw_polygon([[0, 0], [50, 0],[50,100],[0, 100]], 1, 'White', 'Green')
            canvas.draw_polygon([[x*50, 0], [(x+1)*50, 0],[(x+1)*50,100],[x*50, 100]], 1, 'White', 'Green')
    for x in range(0,16):
        if exposed[x] ==True:
            canvas.draw_text(str(deck[x]), (x * 50 ,100), 100, 'Red')



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric