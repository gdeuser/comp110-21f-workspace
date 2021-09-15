"""Finding duplicate letters in a word."""

__author__ = "730306940"

word = input("Enter a word: ")
length = len(word)
x: int = 0
duplicate = False

while x < length:
    letter = word[x]
    y: int = 0
    count: int = 0
    while y < length:
        if word[y] == letter:
            count = count + 1
        y = y + 1
    if count >= 2:
        duplicate = True
    x = x + 1

print("Found duplicate: " + str(duplicate))