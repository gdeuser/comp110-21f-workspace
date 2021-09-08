"""Counting letters in a string."""

__author__ = "730306940"


letter = input("What Letter do you want to search for?: ")
word = input("Enter a word: ")
i: int = 0
final: int = 0

while i < len(word):
    if word[i] == letter:
        final = final + 1
    i = i + 1

print(final)