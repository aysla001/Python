# Coursera: Introduction to Interactive Programming
# Mini Project 4
# AY 20141018
# http://www.codeskulptor.org/#user38_WOizUxRalT_13.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_pos = 340
paddle2_pos = 340
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == "LEFT":
        ball_vel = [-40.0 / 60.0,  -5.0 / 60.0]
    elif direction == "RIGHT":
        ball_vel = [40.0 / 60.0,  -5.0 / 60.0]
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global ball_vel
    global score1, score2  # these are ints
    spawn_ball("LEFT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel
    #1 draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # 4 check if collide with top/bottom
    #if ball_pos[1]<= BALL_RADIUS:
    if ball_pos[1] + BALL_RADIUS > 400:
        ball_vel[1]= -ball_vel[1]
    if ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1]= -ball_vel[1]
        
    # 6 test if ball touches gutter
    if ball_pos[0] <= BALL_RADIUS:
        spawn_ball("RIGHT")
    if ball_pos[0] + BALL_RADIUS > 600:
        spawn_ball("RIGHT")
            
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([0,(paddle1_pos/2)+(PAD_HEIGHT/2)],[0,(paddle1_pos/2)-(PAD_HEIGHT/2)], PAD_WIDTH, "Blue")
    canvas.draw_line([600,(paddle2_pos/2)+(PAD_HEIGHT/2)],[600,(paddle2_pos/2)-(PAD_HEIGHT/2)], PAD_WIDTH, "Blue")
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = - 40.0 / 60.0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 40.0/60.0
    else:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = - 40.0 / 60.0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 40.0/60.0
    else:
        paddle2_vel = 0    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
