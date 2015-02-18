# Learn Python The Hard Way
#Ex41_ObjOriented.py
#Learn to speak object oriented:

#	* class: Tell python to make a new kind of thing
#	* object: an instance of something. the most basic kind of thing.
#	* instance: what you get when you tell Python to create a class.
#	* def: How you define a function inside a class.
#	* self: Inside the functions in a class, self is a variable for the instance/object being accessed.
#	* inheritance: the concept that one class inherits traits from another class.
#	* composition: the concept that a class can be composed of other classes as parts, much like how a car has wheels.
#	* attribute: a property classes have that are from composition and are are usually variables.
#	* is-a: something that inherits from another. "Salmon is-a fish."
#	* has-a: something that is composed of other things. "Salmon has-a mouth."


import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.ord/words.txt"
WORDS = []

PHRASES = {
     "class %%%(%%%):":
          "Make a class named %%% that is-a %%%.",
     "class %%%(object):\n\tdef __init__(self,***)" :
          "class %%% has-a __init__ that takes self and *** parameters.",
     "class %%%(object):\n\tdef ***(self, @@@)":
          "class %%% has-a function named *** that takes self and @@@ parameters.",
     "*** = %%%()":
          "Set *** to an instance of class %%%.",
     "***.***(@@@)":
          "From *** get the *** function, and call it with parameters self, @@@.",
     "***.*** = '***'":
          "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHARSE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
     PHRASE_FIRST = True

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
     WORDS.append(word.strip())

def convert(snippet, phrase):
     class_names = [w.capitalize() for w in
                         random.sample(WORDS, snippet.count("%%%"))]
     other_names = random.sample(WORDS, snippet.count("***"))
     results = []
     param_names = []
    
     for i in range (0, snippet.count("@@@")):
          param_count = random.randint(1,3)
          param_names.append(', '.join(random.samples(WORDS,param_count)))
    
     for sentence in snippet, phrase:
          result = sentence[:]
    
          #fake class names
          for word in class_names:
               result = result.replace("%%%", word, 1)
          #fake other names
          for word in other_names:
               result = result.replace("***", word, 1)
          #fake parameter lists
          for word in param_names:
               result = result.replace("@@@", word, 1)
         
          results.append(result)
     return results

#keep going until they hit CTRL-D
try:
     while True:
          snippets = PHRASES.keys()
          random.shuffle(snippets)
         
          for snippet in snippets:
               phrase = PHRASES[snippet]
               question, answer = convert(snippet, phrase)
               if PHRASE_FIRST:
                    question, answer = answer, question

               print question
              
               raw_input("> ")
               print "ANSWER: %s\n\n" % answer
except EOFError:
     print "\nBye"

Ex41_IsA_HasA_Objects.py

What is the difference between a class and an object. At times they can be the same. For example What is the difference between a Fish and a Salmon?
is-a: Fish and Salmon     has-a: Salmon and Gils

## Animal is-a object look at the extra credit

class Animal(object):
     pass

## Dog is an object
class Dog(Animal):

     def __init__(self, name):
          ## ??
          self.name = name

## ??
class Cat(Animal):

     def __init__(self,name):
          ##??
          self.name = name

##??
class Person(object):

     def __init__(self, name):
          ##??
          self.name = name
         
          ## Person has-a pet of some kind
          self.pet = None

## ??
class Employee(Person):

     def __init__(self, name, salary):
          ## ?? hmm what is this strange magic?
          super(Employee, self).__init__(name)
          ## ??
          self.salary = salary

## ??
class Fish(object):
     pass

## ??
class Salmon(Fish):
     pass

## ??
class Halibut(Fish):
     pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet named satan, note mary has to be defined as above before giving her a pet
mary.pet = satan
print mary.name
print mary.pet.name

## Frank is-a employee making 120000
frank = Employee("Frank", 120000)

## Frank has-a pet named rover
frank.pet = rover
print frank.name
print frank.pet.name
print frank.salary

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()


