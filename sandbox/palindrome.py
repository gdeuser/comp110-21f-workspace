"""Palindrome test for fun."""

phrase = input("Enter a phrase: ")
length = len(phrase)
x: int = 0
y = length - 1
palindrome = True

while x < y:
    if phrase[x] != phrase[y]:
        palindrome = False
    x = x + 1
    y = y - 1

print("Palindrome: " + str(palindrome))