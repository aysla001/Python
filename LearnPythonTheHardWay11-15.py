# Learn Python The Hard Way
# Exercise 11 (ex11_input.py)
print "How old are you?",
age = raw_input()
# collect age
print "How tall are you?",
height = raw_input()
# collect height
print "How much do you weigh?",
weight = raw_input()
# collect weight

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
#print it out

#Notice that we put a , (comma) at the end of each print line. This is so that print doesn't end the line with a newline character and go to the next line.

# Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?

#	* print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
#	* print "So you're %s old, %s tall and %s heavy." % (age, height, weight)
#	* Remember %r is for debugging and is "raw representation" while s is for display     

# Exercise 12 (ex12_input.py)
#consolidated version of exercise 11
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

 -m pydoc raw_input     #python documentation


# Exercise 13 (ex13_para_unpack_var.py)
from sys import argv
#modules = libraries
script, first, second, third = argv      # tells me how many arguments

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
#whatever is in argv unpack it and assign to all of these variables on the left in order
#$ python ex13.py first 2nd 3rd
#prints out below
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

# argv vs raw_input()
#     difference is where the user is required to give input. If they give your script inputs on the command line then use argv. If you want to collect input using the keyboard while the script is running, then use raw_input().


# Exercise 14 (ex14_prompt_pass.py)
from sys import argv

script, user_name = argv # 1 argument
prompt = '()' # value to prompt for input.

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer)

# Exercise 15 (ex15_reading_files.py)
from sys import argv

script, filename = argv

txt = open(filename) # opens text file

print "Here's your file %r:" % filename # prints the name of the file
print txt.read() # function on the opened text file # print the text file
txt.close()

print "Type the filename again:"
file_again = raw_input("> ") # prompt user with >

txt_again = open(file_again)

print txt_again.read()
txt_again.close()


