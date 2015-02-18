# Coursera: Introduction to Interactive Programming
# Mini Project 1
# AY 20141001
# http://www.codeskulptor.org/#user38_dZTrSGpKps_13.py


import random

def name_to_number(name):
    if name=='rock':
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("incorrect selection")

def number_to_name(number):
    if number==0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("incorrect selection")
    print name

def rpsls(player_choice):
    print
    print("Player chooses " + player_choice)
    player_choice_num = name_to_number(player_choice)
    computer_guess = random.randrange(0, 5, 1)
    computer_guess_name = number_to_name(computer_guess)
    # each choice wins against the preceding two choices and loses against the following two choices 
    #(if rock and scissors are thought of as being adjacent using modular arithmetic).
    print ("Computer chooses " + computer_guess_name)
    difference= (player_choice_num - computer_guess) % 5
    #print difference
    if difference == 0:
        print ("TIE!")
    elif difference <= 2:
        print ("Player wins!")
    elif difference >2:
        print ("Computer wins!")

rpsls("scissors")