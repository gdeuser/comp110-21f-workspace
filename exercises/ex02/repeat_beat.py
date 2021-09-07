"""Repeating a beat in a loop."""

__author__ = "730306940"


beat = input("What beat do you want to repeat? ")
beat = beat + " "
repeat: int = int(input("How many times do you want to repeat it? "))
count: int = 0
while count < repeat:
    if repeat > 0:
        print(str(beat * repeat))
    else:
        print("No beat...")
    count = repeat