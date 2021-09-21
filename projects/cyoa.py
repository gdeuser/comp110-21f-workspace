"""Choose Your Own Adventure Project."""

__author__ = 730306940


def main() -> None:
    """The program's entrypoint."""
    points: int = 0
    greet()


def greet() -> None:
    """Introducing the program to adventurer."""
    print("Hello and welcome to the adventure of a lifetime.")
    player = input("What is your name? ")


print(player) 

if __name__ == "__main__":
    main()