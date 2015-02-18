# Learn Python The Hard Way
# Ex38_DoThingsToLists.py

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split (' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
     next_one = more_stuff.pop()
     print "Adding: ", next_one
     stuff.append(next_one)
     print "There's %d items now."  % len (stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff [1]
print stuff [-1]
print stuff.pop()
print ' '.join(stuff)               #Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print '#'.join(stuff[3:5])      #Telephone#Light
##Why does join(' ', stuff) not work?  Rewrite it like ' '.join(stuff).

#Ex39_Dictionaries.py
#You can use "index" into a list, meaning you can use numbers to find out what's in lists. You can only use numbers to get items out of a list. A dict will let you use anything, not just numbers.
#create a mapping of state to abbreviation
states ={
     'Oregon': 'OR',
     'Florida': 'FL',
     'California': 'CA',
     'New York': 'NY',
     'Michigan': 'MI'
}
#creates a basic set of states and some cities in them
cities = {
     'CA': 'San Francisco',
     'MI': 'Detroit',
     'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
     print "%s has the city %s" % (state, abbrev)

#print every city in state
print '-' * 10
for abbrev, city in cities.items():
     print "%s has the city %s" % (abbrev,city)

#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
     print "%s states is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
     print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for state'TX' is: %s" % city
