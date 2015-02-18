# Learn Python The Hard Way
# Exercise 6


x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# %r for debugging since it displays the raw, others are for display
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# adding strings together appends the two strings together
print w + e


# Exercise 7 (ex7_printing.py)
print "Mary had a little lamb."
print "Its fleece was white as %s." %'snow'
print "And everywhere that Mary went."
print "." * 10 #what'd that do? #prints 10 *

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11  = "e"
end12 = "r"

#watch that comma at the end. try removing it to see what happens
#the comma puts it all on one line with no spaces Cheese Burger
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 +end12

# Exercise 8 (ex8_printing_formatter.py)
formatter = "%r %r %r %r"

print formatter %(1, 2, 3, 4)
# prints 1 2 3 4
print formatter % ("one", "two", "three", "four")
# prints 'one" "two" "three" "four"
print formatter % (True, False, False, True)
# prints True False False True
print formatter % (formatter, formatter, formatter, formatter)
# prints '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (
     "I had this thing.",
     "That you could type up right.",
     "But it didn't sing.",
     "So I said goodnight."
     )
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'


# Exercise 9 (ex9_more_printing.py)
days = "Mon Tue Wed Thu Fri Sat Sun"
# prints everything on one line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# prints everything on separate lines

#Why do the \n newlines not work when I use %r?That's how %r formatting works; it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.Why do I get an error when I put spaces between the three double-quotes?You have to type them like """ and not " " ", meaning with no spaces between each one.

# Exercise 10
#There are plenty of these "escape sequences" available for different characters you might want to put in, but there's a special one, the double backslash, which is just two of them \\. These two characters will print just one backslash.
#Another important escape sequence is to escape a single-quote ' or double-quote ". Imagine you have a string that uses double-quotes and you want to put a double-quote in for the output. 

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat good
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
#prints      I'm tabbed in.
print persian_cat
#prints I'm slot
# on a line
print backslash_cat
#prints I'm \ a \ cat
print fat_cat






