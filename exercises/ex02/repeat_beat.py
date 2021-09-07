"""Repeating a beat in a loop."""

__author__ = "730306940"


beat = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))

count: int = 0
while count < repeat:
    if repeat > 0:
        beat_2 = beat + str(" " + beat)
        count = count + 1
        print(beat)
    else:
        print("No beat...")