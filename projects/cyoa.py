"""Choose Your Own Adventure Project."""

__author__ = 730306940

points: int
player = ""
NAMED_CONSTANT = "\U0001F920"


def main() -> None:
    """The program's entrypoint."""
    global points
    stopped = False
    points = 0
    greet()
    while not stopped:
        select: int = int(input("Choose 1 for basketball, 2 for football , and 3 to quit and save your ego. "))
        if select == 3:
            stopped = True
        else:
            if select == 2:
                football()
            else:
                if select == 1:
                    points = basketball(points)
                else:
                    print("Put in a valid number, coward.")
        print(f"So far, you have accumulated {points} fan points.")
    print(f"Hey {player}, your points are {points}.")
    print(NAMED_CONSTANT)
    print(fan_evaluator(points))


def greet() -> None:
    """Introducing the program to adventurer."""
    global player
    player = input("What is your name? ")
    print(f"Hey {player}, welcome to the ultimate UNC fan evaluator! Take this test at your own risk - the programmer is not responsible for any hurt feelings that come from your lack of Tar Heel knowledge. ")


def basketball(current_points: int) -> int:
    """Asking UNC basketball trivia."""
    from random import randint
    basketball_points: int = 0
    random_question = randint(1, 2)
    if random_question == 1:
        basketball_points = basketball_points + 1
    return(current_points + basketball_points)


def football() -> None:
    """Trivia about UNC football."""
    global player
    global points
    coach: int = int(input("Who is the football head coach? Type 1 for Mack Brown. Type 2 for Roy Williams. Type 3 for Kevin G. "))
    if coach == 1:
        print(f"Good work, {player}!")
        points = points + 5
    else:
        if coach == 2:
            print("Well, at least your answer was in the world of UNC sports...")
            points = points + 1
        else:
            if coach == 3:
                print("Are you even a UNC sports fan? I'm disappointed.")
                points = points - 7
            else:
                print(f"Thought you were being sneaky by not giving a proper response, {player}? You lose a point.")
                points = points - 1


def fan_evaluator(current_points: int) -> str:
    """Saying what type of fan the test-taker is."""
    global player
    fan_type = ""
    if current_points < 4:
        fan_type = f"{player}, you must cheer for Duke."
    else:
        if current_points < 15:
            fan_type = f"Must admit, you are an exceptionally average fan, {player}."
        else:
            fan_type = f"Wow {player}, someone needs to get a building on campus named after you becuase of all your impressive UNC sports knowledge!"
    return(fan_type)


if __name__ == "__main__":
    main()