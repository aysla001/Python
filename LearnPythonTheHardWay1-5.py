# Learn Python The Hard Wayxercise 4: math, print, and variables
# excercise 4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."



#exercise 5: math, advanced printing, and variables
my_name = 'Zed A. Shaw'
my_age = 35
# notice the use of the % and how it prints things without a space.
print "Let's talk about %s." %my_name
print "My name is %s and my age is %d." % (my_name, my_age)




