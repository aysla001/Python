# Learn Python The Hard Way
#Ex40_Modules.py
#Modules are like dictionaries.

#	* You know how a dictionary is created and used and that it is a way to map one thing to another. That means if you have a dictionary with a key 'apple' and you want to get it then you do this:
mystuff = {'apple' : "I AM APPLES!"}
print mystuff['apple']
	* Imagine if I have a module that I decide to name mystuff.py and I put a function in it called apple. 
def apple():
     print "I AM APPLES!"
tangerine = "Living reflection of a dream"
--------new file----
import mystuff
mystuff.apple()             # will print "I AM APPLES!"
print mystuff.tangerine  # because of the print command will print tangerine variable from mystuff.py 

#Classes are like modules

# * module is a specialized dictionary that can store Python code so that you can get to it with the "." operator. 
# * A class is similar. It takes a grouping of functions and data and place them inside a container so you can access them with the "." (dot) operator.
# * if we add the below to the mystuff module Not sure if this is possible? I had to add this directly into ex40_1_modules.py


def __init__(self):
     self.tangerine = "And now a thousand years between"
def apple(self):
     print "I AM CLASSY APPLES!"
	* we yse classes instead of modules to take as many instances as we want of the objects. With modules there is only one for the entire program.

#Objects are like mini imports

#	* if a class is like a mini-module then there has to be a similar concept to import (instantiate).


ex40_2_modules.py
class Song(object):
     def __init__(self, lyrics):
          self.lyrics = lyrics
     def sing_me_a_song(self):
          for line in self.lyrics:
               print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued",
                         "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                              "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()



