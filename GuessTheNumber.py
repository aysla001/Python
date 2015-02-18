# Coursera: Introduction to Interactive Programming
# Mini Project 2
# AY 201411


# import libraries to be used
import simplegui
import random
import math

# initialize global variables for random number, highest guess under, lowest guess over, and number of guesses
random_number = 0
highest_guess_under = -1
lowest_guess_over = 1000000000
current_number_guesses = 0 


# helper function to initial game
def init():
    range100()
    
# define handler to create random number for 0 - 100 range
## also clear out current number of guesses when button pressed
def range100():
    print "Welcome Please Select a Number 0 - 100"
    global random_number
    global current_number_guesses
    random_number = random.randrange(0, 100)
    current_number_guesses = 0 
    
    ## need to reset these in range handlers for when button is pressed
    global highest_guess_under
    global lowest_guess_over
    highest_guess_under = -1
    lowest_guess_over = 1000000000

# define handler to create random number for 0 - 1000 range
## also clear out current number of guesses when button pressed
def range1000():
    print "Welcome Please Select a Number 0 - 1000"
    global random_number
    global current_number_guesses
    random_number = random.randrange(0, 1000)
    current_number_guesses = 0
    
    ## need to reset these in range handlers for when button is pressed
    global highest_guess_under
    global lowest_guess_over
    highest_guess_under = -1
    lowest_guess_over = 1000000000

# define handler for handling input
## will take input and determine if it is too high or too low and how many guesses remain
## if number of guesses reaches zero calls range100() to restart game
def input_guess(guess):
    #turn input string into integer
    guess = int(guess)
    global random_number
    global highest_guess_under
    global lowest_guess_over
    global current_number_guesses
    #increment current_number_guesses since a new input has been received
    current_number_guesses = current_number_guesses + 1
    if random_number < 100:
        max_number_guesses= 7
    else :
        max_number_guesses = 10
    if guess == random_number:
        print "Correct. Game Restart"
        range100()
    
    #if guess is less the random number determine if it is the new highest guess under and how many guesses remain
    elif guess < random_number:
        if highest_guess_under == -1:
            highest_guess_under = guess
            print "Higher. Number of guesses remaining ", max_number_guesses - current_number_guesses
        elif guess > highest_guess_under:
            highest_guess_under = guess
            print "Higher. Number of guesses remaining ", max_number_guesses - current_number_guesses, ". Closest guess under is", highest_guess_under
        elif guess < highest_guess_under:
            print "Higher. Number of guesses remaining ", max_number_guesses - current_number_guesses, ". Closest guess under is", highest_guess_under
    
    #if guess is over the random number determine if it is the new lowest guess over and how many guesses remain
    elif guess > random_number:
        if lowest_guess_over == 1000000000:
            lowest_guess_over = guess
            print "Lower. Number of guesses remaining ", max_number_guesses - current_number_guesses
        elif guess < lowest_guess_over:
            lowest_guess_over = guess
            print "Lower. Number of guesses remaining ", max_number_guesses - current_number_guesses, ". Closest guess over is", lowest_guess_over
        elif guess >lowest_guess_over:
            print "Lower. Number of guesses remaining ", max_number_guesses - current_number_guesses, ". Closest guess over is", lowest_guess_over
    
    ##if no guesses remain go back to range 0 - 100
    if max_number_guesses-current_number_guesses == 0:
        print "Reset"
        init()

    
#create window(s)
f = simplegui.create_frame ("Guess the number", 200,200)

# create control elements for window
f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Enter a guess", input_guess, 200)

#initialize
init()