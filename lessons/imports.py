"""Examples of imports."""

from lessons import helpers

# Import using an alias
from lessons import helpers as hp

# Import names directly from globals of a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    # Access the first import
    print(helpers.powerful(2, 4))

    # Access the alias import
    print(hp.THE_ANSWER)

    # Call the imported function directly
    print(powerful(2, 10))
    print(THE_ANSWER)

    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()