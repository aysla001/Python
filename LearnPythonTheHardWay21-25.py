# Learn Python The Hard Way
# ex21_Functions_Return.py
def add(a, b):
     print "ADDING %d + %d" % (a, b)
     return a + b

def subtract(a, b):
     print "SUBTRACTING %d - %d" % (a, b)
     return a - b

def multiply(a, b):
     print "MULTIPLY %d * % d" % (a, b)
     return a * b

def divide(a, b):
     print "DIVIDING %d / %d" % (a, b)
     return a / b


print "Let's do some math with just functions!"
age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height %d, Weight %d, IQ: %d" % (age, height, weight, iq)
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"
# ex22_What do you know so far?
# It's important when you are doing a boring, mindless memorization exercise like this to know why. It helps you focus on a goal and know the purpose of all your efforts.
# In this exercise you are learning the names of symbols so that you can read source code more easily. It's similar to learning the alphabet and basic words of English, except this Python alphabet has extra symbols you might not know.

# ex23_Read Some Code
#	1. Finding Python source code for things you need.
#	2. Reading through the code and looking for files.
#	3. Trying to understand code you find.
#	1. Go to bitbucket.org, github.com, or gitorious.org with your favorite web browser and search for "python."
#	2. Avoid any project that mentions "Python 3". That'll only confuse you.
#	3. Pick a random project and click on it.
#	4. Click on the Source tab and browse through the list of files and directories until you find a .py file (but not setup.py, that's useless).
#	5. Start at the top and read through it, to take notes on what you think it does.
#	6. If any symbols or strange words seem to interest you, write them down to research later.

#ex24_MorePractice.py
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanationE\n\t\twhere there is none.
"""

print "-------------"
print poem
print "-------------"


five = 10 - 2 + 3 - 6
print "This should be five %s" % five

def secret_formula(started):
     jelly_beans = started * 500
     jars = jelly_beans / 1000
     crates = jars / 100
     return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#ORDER IS IMPORTANT SHOULD MATCH FUNCTION

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# ex25_PracticePopping.py

def break_words(stuff):
     """This function will break up words for us."""
     words = stuff.split(' ')
     return words

def sort_words(words):
     """Sorts the words."""
     return sorted(words)
          ## note sorted function

def print_first_word(words):
     """Prints the first word after popping it off."""
     word = words.pop(0)
     print word
          ##note popping

def print_last_word(words):
     """Prints the last word after popping it off."""
     word = words.pop(-1)
     print word
          ##note popping

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


