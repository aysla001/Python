# Learn Python The Hard Way
# Inheritance is used to indicate that one class will get most or all of its features from a parent class.
# Happens implicitly when you write Foo(Bar). Common functionality goes in the Bar class, then specialize that functionality in the Foo class as needed.


#	1. Actions on the child imply an action on the parent.
#	2. Actions on the child override the action on the parent.
#	3. Actions on the child alter the action on the parent.

# Implicit Inheritance: actions that happen when you define a function in the parent, but not in the child.
class Parent(object):
def implicit(self):
print "PARENT implicit()"

class Child(Parent):
pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()  # even though child does not have an implicit function defined it still works and calls the parent one.
#####Returns ####
PARENT Implicit()

Alter Before or After: 
class Parent(object):
def altered(self):
print "PARENT altered()"

class Child(Parent):
def altered(self):
print "CHILD, BEFORE PARENT altered()"
super (Child, self).altered()
print "CHILD, AFTER PARENT altered()"

dad = Parent ()
son = Child()

dad.altered()
son.altered()
#####Returns ####
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()

All Thee Combined:
class Parent(object):
     def override(self):
          print "PARENT override()"
     def implicit(self):
          print "PARENT implicit()"
     def altered(self):
          print "PARENT altered()"
class Child(Parent):
     def override(self):
          print "CHILD override()"
     def altered(self):
          print "CHILD, BEFORE PARENT altered()"
          super(Child, self).altered()
          print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()          # prints PARENT implicit()
son.implicit()          # prints PARENT implicit()

dad.override()          # prints PARENT override
son.override()          # prints CHILD override

dad.altered()          #prints PARENT altered()
son.altered()          # prints CHILD, BEFORE PARENT altered then prints CHILD, AFTER PARENT altered

Multiple Inheritance: When you define a class that inherits from one or more classes.
class SuperFun (Child, BadStuff):
     pass
# like saying make a class with SuperFun that inherits from Child class and BadStuff at the same time.

	* Whenever you have implicit actions on any SuperFun instance, Python has to look-up the possible function in the class hierarchy for both Child and BadStuff, but it needs to do this in a consistent order. (Method Resolution Order MRO and an algorithm called C3)
	* Because MRO and C3 is complext Python uttilizes super()
	* the most common use of super is in __init__ functions in base elements.
	* This because this is the only place where you need to do some things in a chile, then complete the initialization in the parent.
class Child(Parent):
     def __init__ (self, stuff):
           self.stuff = stuff
           super(Child, self).__init__()

Composition: Instead of using inheritance you can use other classes and modules. 
class Other(object):
     def override(self):
          print "OTHER override()"
     def implicit(self):
          print "OTHER implicit()"
     def altered(self):
          print "OTHER altered()"
class Child (object):
     def __init__(self):
          self.other = Other()
     def implicit(self):
          self.other.implicit()
     def override(self):
          print "CHILD override()"
     def altered(self):
          print "CHILD, BEFORE OTHER altered()"
          self.other.altered()
          print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()
#### returns below ####
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()


#	* In this code we are not using the name Parent since there is not a parent-child-is-a relationship.
#	* There is a has-a relationship, where the Child has-a other

# When to use inheritance or composition: Problem of reusable code.
 
#	1. Avoid multiple inheritance. If you have to understand class hierarchy.
#	2. Use composition to package up code into modules that are used in many different unrelated places and situations.
#	3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.

#Aren't objects just copies of classes? True in JavaScript not true in Python. In Python, classes act as templates that "mint" new objects, similar to how coins were minted using a die (template).



