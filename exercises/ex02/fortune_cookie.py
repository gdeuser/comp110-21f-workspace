"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730306940"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

fortune = randint(1, 50)
print("Your fortune cookie says...")
if fortune > 38:
    print("You will succeed in all of your endeavors.")
else:
    if fortune >= 25:
        print("In three days time, something unexpectedly good will happen.")
    else:
        if fortune > 13:
            print("You will experience an event of great pleasure this week.")
        else:
            print("Soon, you will find the only truth that can satisfy your soul.")
print("Now, go spread positive vibes!")