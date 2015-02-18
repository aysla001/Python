# Learn Python The Hard Way
# Exercise 16 Reading and Writing Files
#	* close -- Closes the file. Like File->Save.. in your editor.
#	* read -- Reads the contents of the file. You can assign the result to a variable.
#	* readline -- Reads just one line of a text file.
#	* truncate -- Empties the file. Watch out if you care about the file.
#	* write(stuff) -- Writes stuff to the file.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file.."
target = open (filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# Exercise 17 More Files (Copy files)

You should immediately notice that we import another handy command named exists.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file).read()
#indata = in_file.read()

print "The input file is %d bytes long" % len(in_file)

print "does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w').write(in_file)
#out_file.write(indata)

print "Alright, all done."

#out_file.close()
#in_file.close()

You do not need to close files if you do the single line open and read.

# Ex18_Nam_Var_Code_Fxn.py

# this one is like your scripts with argv
def print_two(*args):
     arg1, arg2 = args
     print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
     print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one arguement
def print_one(arg1):
     print "arg1: %r" % arg1

#this one takes no arguements
def print_none():
     print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

Did you start your function definition with def?
Does your function name have only characters and _ (underscore) characters?
Did you put an open parenthesis ( right after the function name?
Did you put your arguments after the parenthesis ( separated by commas?
Did you make each argument unique (meaning no duplicated names)?
Did you put a close parenthesis and a colon ): after the arguments?
Did you indent all lines of code you want in the function four spaces? No more, no less.
Did you "end" your function by going back to writing with no indent (dedenting we call it)?
And when you run ("use" or "call") a function, check these things:

Did you call/use/run this function by typing its name?
Did you put the ( character after the name to run it?
Did you put the values you want into the parenthesis separated by commas?
Did you end the function call with a ) character?


# Ex19_More_Fxn_Var.Py
def cheese_and_crackers(cheese_count, boxes_of_crackers):
     print "You have %d cheeses!" % cheese_count
     print "You have %d boxes of cracker!" % boxes_of_crackers
     print "Man that's enough for a party!"
     print "Get a blanket.\n"

     print "We can just give the functions numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Ex20_Fxn_Files.py
python Ex20_Fxn_Files.py("test.txt")

from sys import argv
script, input_file = argv
def print_all(f):
     print f.read()
def rewind(f):
     f.seek(0)
def print_a_line(line_count, f):
     print line_count, f.readline()

current_file = open(input_file)
print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)



