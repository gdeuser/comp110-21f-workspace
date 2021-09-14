"""Drawing forests in a loop."""

__author__ = "730306940"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
tree: str = '\U0001F332'
depth: int = int(input("Depth: "))
start: int = 1

while start > 0 and start <= depth:
    print(tree)
    tree = tree + TREE
    start = start + 1