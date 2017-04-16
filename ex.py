#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input('-->')
#print "How much do you weigh?",
#weight = raw_input()

#print "so you are %r years old, %r tall and %r heavy." % (age, height, weight)
from sys import argv

script, first, second = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
third = raw_input("third?: ")
fourth = raw_input("fourth?: ")
print "Your third variable is:", third
print "Your fourth variable is: ", fourth
