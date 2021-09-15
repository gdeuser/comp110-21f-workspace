"""Drawing forests in a loop."""

__author__ = "730306940"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
tree = ""
depth: int = int(input("Depth: "))

while depth > 0:
    depth = depth - 1
    tree = tree + TREE
    print(tree)