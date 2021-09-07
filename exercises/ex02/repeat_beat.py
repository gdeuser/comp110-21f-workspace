"""Repeating a beat in a loop."""

__author__ = "730306940"


beat = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
count: int = 0
v = ""

if repeat <= 0:
    print("No beat...")
else:
    while count < repeat:
        if count == repeat - 1:
            v = v + beat
        else:
            v = v + beat + " "
        count = count + 1
print(v)