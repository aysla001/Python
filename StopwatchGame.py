# Coursera: Introduction to Interactive Programming
# Mini Project 3
# AY 201411
# http://www.codeskulptor.org/#user4-cn999X9MuXzCC0X-4.py

import simplegui
import random
import math

# define global variables
canvas_width = 500
canvas_height = 500
game_timer_text = "0:00:00"
game_time = 0
success = 0
attempts = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global game_timer_text
    minutes = int(game_time / 60000)
    seconds = int((game_time - (minutes * 60000)) / 1000)
    ms = game_time - (minutes * 60000) - (seconds * 1000)
    minutes = str(minutes)
    seconds= str(seconds)
    ms= str(ms)
    game_timer_text = minutes + ":" + seconds + ":"+ ms 
    print game_time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global game_timer_text
    game_timer.start()
    #game_timer_text= str(game_timer)
    #print "Start" , game_time

def stop_button():
    global attempts
    game_timer.stop()
    game_time = str(game_timer)
    attempts = int(attempts)
    attempts +=1
    print game_time
    
def reset_button():
    global game_time
    game_time =0 
    

# define event handler for timer with 0.1 sec interval
def increment ():
    global game_time
    game_time += 1

    
# create frame
def draw(canvas):
    global success, attempts
    format(game_time)
    canvas.draw_text(game_timer_text, [canvas_width/4, canvas_height/2], 60, "Red")
    success = str(success)
    canvas.draw_text("Successes: " + success, [canvas_width- 155, canvas_height-470], 20, "Blue")
    attempts= str(attempts)
    canvas.draw_text("Attempts: " + attempts, [canvas_width- 155, canvas_height-437], 20, "Blue")
    

frame = simplegui.create_frame ("Game Timer", canvas_width, canvas_height)
frame.set_draw_handler(draw)

# register event handlers

frame.add_button("Start", start_button, 75)
frame.add_button("Stop", stop_button, 75)
frame.add_button ("Reset", reset_button, 75)

# start timer and frame
game_timer = simplegui.create_timer(1,increment)
#stop_timer = simplegui.create_timer(1,increment)

frame.start()

# remember to review the grading rubric
