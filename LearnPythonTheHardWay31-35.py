# Learn Python The Hard Way
# Ex31_MakingDecisions.py
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
print "There's a giant bear here eating a cheese cake. What do you do?"
print "1. Take the cake."
print "2. Scream at the bear."
bear = raw_input("> ")
if bear == "1":
print "The bear eats your face off. Good job!"
elif bear == "2":
print "The bear eats your leg off. Good job!"
else:
print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
print "You stare into the endless abyss at the Cthulu's retina."
print "1. Blueberries."
print "2. Yellow jacket clothespins."
print "3. Understanding revolvers yelling melodies."

insanity = raw_input("> ")
if insanity == "1" or insanity == "2":
print "Your body survives powered by a mind of jello. Good job!"
else:
print "The insanity rots your eyes into a pool of muck. Good job!"

else:
print "You stumble around and fall on a knife and die. Good job!"

# Ex32_LoopsListst
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
     print "This is count %d" % number

# same as above
for fruit in fruits:
     print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
     print "I got %r" %i

#we can also built lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts.
# range gives us all the numbers in a range () but does not include those numbers (0,6) include 1,2,3,4,5
for i in range (0,6):
     print "Adding %d to the list." % i
     #append is a function that lists understand
     elements.append(i)

#not we can print them out too
for i in elements:
     print "Element was: %d" % i

# ex33_WhileLoops.py
def wloop(max, inc):
     i = 0
     numbers = []
     while i < max:
          print "At the top i is %d" % i
          numbers.append(i)
          i = i + inc
          print "Numbers now: ", numbers
          print "At the bottom i is %d" % i
     print "The numbers: "
     for num in numbers:
          print num

wloop(15,2)
ex34_ElementsOfLists.py
Python starts lists at 0. Ordinal vs cardinal numbers
List[element]
Dijsktra

# ex35_BranchesFunctions.py

from sys import exit

def gold_room():
     print "This room is full of gold. How much do you take?"
    
     next = raw_input("> ")
     if "0" in next or "1" in next:
          how_much = int(next)
     else:
          dead("Man, learn to type a number.")

     if how_much < 50:
          print "Nice, you're not greedy, you win!"
          exit(0)
     else:
          dead("You greedy bastard!")

def bear_room():
     print "There is a bear here."
     print "The bear has a bunch of honey."
     print "The fat bear is in front of another door."
     print "How are you going to move the bear?"
     bear_moved = False

     while True:
          next = raw_input("> ")
         
          if next == "take honey":
               dead("The bear looks at you then slaps your face off.")
          elif next == "taunt bear" and not bear_moved:
               print "The bear has moved from the door. You can go through it now."
               bear_moved = True
          elif next == "taunt bear" and bear_moved:
               dead("The bear gets pissed off and chews your leg off.")
          elif next == "open door" and bear_moved:
               gold_room()
          else:
               print "I got no idea what that means."

def cthulu_room():
     print "Here you see the great evil Cthulu."
     print "He, it, whatever stares at you and you go insane."
     print "Do you flee for your life or eat your head?"
    
     next = raw_input("> ")
    
     if "flee" in next:
          start()
     elif "head" in next:
          dead("Well that was tasty!")
     else:
          cthulu_room()

def dead(why):
     print why, "Good job!"
     exit(0)

def start():
     print "You are in a dark room."
     print "There is a door to your right and left."
     print "Which one do you take?"
    
     next = raw_input("> ")
    
     if next == "left":
          bear_room()
     elif next == "right":
          cthulu_room()
     else:
          dead("You stumble around the room until you start.")

start()






