# Learn Python The Hard Way
# Ex26_Fix.py

#	1. copy python from http://learnpythonthehardway.org/book/exercise26.txt
#	2. note used import ex25_PracticePopping to import import ex25_PracticePopping.py
#	3. debug

import ex25_PracticePopping
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)


sentence = "All god\t things come to those who weight."

words = ex25_PracticePopping.break_words(sentence)
sorted_words = ex25_PracticePopping.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25_PracticePopping.sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)

# Ex27_MemorizingLogic
# and
# or
# not
# != (not equal)
# == (equal)
# >= (greater-than-equal)
# <= (less-than-equal)
# True
# False
#Ex28_BooleanPractice

	* Find an equality test (== or !=) and replace it with its truth.
	* Find each and/or inside parentheses and solve those first.
	* Find each not and invert it.
	* Find any remaining and/or and solve it.
	* When you are done you should have True or False.

You can run python directly in PowerShell 
enter python (just type python and hit enter in PowerShell)
>>> 1 == 1
# will evaluate as either True or False

Ex29_WhatIf.py
people = 20
cats = 30
dogs = 15

if people < cats:
print "Too many cats! The world is doomed!"

if people > cats:
print "Not many cats! The world is saved!"

if people < dogs:
print "The world is drooled on!"

if people > dogs:
print "The world is dry!"

dogs += 5

if people >= dogs:
print "People are greater than or equal to dogs."

if people <= dogs:
print "People are less than or equal to dogs."

if people == dogs:
print "People are dogs."
Ex30_ElseAndIf.py

people = 30
cars = 40
buses = 15

if cars > people:
print "We should take the cars."
elif cars < people:
print "We Should not take the cars."
else:
print "We can't decide."

if buses > cars:
print "That's too many buses."
elif buses < cars:
print "Maybe we could take the buses."
else:
print "We still can't decide."

if people > buses:
print "Alright, let's just take the buses."
else:
print "Fine, let's stay home then."

#What happens if multiple elif blocks are True?
#Python starts and the top at runs the first block that is True, so it will run only the first one.

