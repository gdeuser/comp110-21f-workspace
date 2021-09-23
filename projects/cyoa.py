"""Choose Your Own Adventure Project."""

__author__ = 730306940

points: int
player: str = ""
COWBOY_HAT: str = "\U0001F920"
BUILDING: str = "\U0001F3EB"
DUKE: str = "\U0001F47F"
STAR: str = "\U0001F31F"
RAM: str = "\U0001F40F"
BASKETBALL_EMOJI: str = "\U0001F3C0"
FOOTBALL_EMOJI: str = "\U0001F3C8"


def main() -> None:
    """The program's entrypoint."""
    global points
    stopped: bool = False
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
    print(f"Hey! You! Yeah you, {player}! Drum roll PLEASE...")
    print("AAAAND your FINAL total of fan points for all your correct and incorrect guesses is...")
    print(COWBOY_HAT)
    print(f"{points}.")
    print(fan_evaluator(points))


def greet() -> None:
    """Introducing the program to adventurer."""
    global player
    player = input("State your name for the record. ")
    print(f"Hey {player}, welcome to the ultimate UNC fanalyzer test! {STAR} Take this test at your own risk - the programmer is not responsible for any hurt feelings that come from your lack of Tar Heel knowledge. Think you're a Tar Heel born, bred, dead? {RAM} Have a crack at this test to find out!")


def basketball(current_points: int) -> int:
    """Asking UNC basketball trivia."""
    from random import randint
    basketball_points: int = 0
    random_question: int = randint(1, 3)
    if random_question == 1:
        leaky: int = int(input(f"{BASKETBALL_EMOJI} What is Leaky Black's real first name? Type 1 for Duwe. Type 2 for Rechon. Type 3 for Dontrez. "))
        if leaky == 1:
            print(f"That's the name of another player on the roster, {player}.")
            basketball_points = basketball_points - 2
        else:
            if leaky == 2:
                print("Rechon Leaky Black. A powerful name for a powerful player. ")
                basketball_points = basketball_points + 4
            else:
                if leaky == 3:
                    print(f"I would say you were close, {player}, but you really weren't.")
                    basketball_points = basketball_points - 2
                else:
                    print(f"Really, {player}, really?")
                    basketball_points = basketball_points - 1

    else:
        if random_question == 2:
            coach: int = int(input(f"{BASKETBALL_EMOJI} Who is the current head coach? Type 1 for Annson Dorrance. Type 2 for Roy Williams. Type 3 for Hubert Davis. "))
            if coach == 1:
                print("You shoot, you score, but in soccer not basketball...")
                basketball_points = basketball_points - 3
            else:
                if coach == 2:
                    print("The wound of his retirement is too fresh for you to be guessing that right now. ")
                else:
                    if coach == 3:
                        print(f"Absolutely correct, {player}. Heck yes he's the head coach. ")
                        basketball_points = basketball_points + 5
                    else:
                        print(f"Please give an actual guess next time, {player}.")
                        basketball_points = basketball_points - 1
        else:
            ball: int = int(input(f"{BASKETBALL_EMOJI} What is the name of the actual court that the basketball team plays on insdie the Dome? Type 1 for Dean Smith Court. Type 2 for Michael Jordan Court. Type 3 for Roy Williams Court. "))
            if ball == 1:
                print(f"I can see how you thought this, {player}, but simply no <3.")
                basketball_points = basketball_points - 2
            else:
                if ball == 2:
                    print(f"{player}, he might be the GOAT, but the court is certainly not named after MJ.")
                    basketball_points = basketball_points - 2
                else:
                    if ball == 3:
                        print("Yes!!!")
                        basketball_points = basketball_points + 5
                    else:
                        print("You're losing points as I code.")
                        basketball_points = basketball_points - 1
    return(current_points + basketball_points)


def football() -> None:
    """Trivia about UNC football."""
    global points
    coach: int = int(input(f"{FOOTBALL_EMOJI} Who is the football head coach? Type 1 for Mack Brown. Type 2 for Roy Williams. Type 3 for Kevin Guskiewicz. "))
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
    record: int = int(input(f"{FOOTBALL_EMOJI} What was the Tarheel's final record at the end of the 2020 season? Type 1 for 9-1. Type 2 for 4-6. Type 3 for 7-3. "))
    if record == 1:
        print("At least you're optimistic! But still incorrect.")
    else:
        if record == 2:
            print(f"Really, {player}, thinking we had a losing season? With Sam Howell? The audacity.")
            points = points - 3
        else:
            if record == 3:
                print(f"{player}, you really know your stuff!")
                points = points + 3
            else:
                print(f"You just lost points for that answer, {player}.")
                points = points - 1
    offense: int = int(input(f"{FOOTBALL_EMOJI} Who is UNC's Offensive Coordinator? Type 1 for Phil Longo. Type 2 for Jovan Dewitt. Type 3 for Storm Duck. "))
    if offense == 1:
        print(f"I'm impressed that you knew that, {player}!")
        points = points + 6
    else:
        if offense == 2:
            print("He's special teams coach, not offensive coordinator.")
            points = points - 1
        else:
            if offense == 3:
                print(f"{player}, He is the defensive back. Good try!")
                points = points - 3
            else:
                print(f"Cmon {player}, you can't just be throwing away fan points like this!")
                points = points - 1


def fan_evaluator(current_points: int) -> str:
    """Saying what type of fan the test-taker is."""
    fan_type: str = ""
    if current_points < 7:
        fan_type = f"{player}, you must cheer for Duke. {DUKE}"
    else:
        if current_points < 17:
            fan_type = f"Must admit, you are an exceptionally average fan, {player}."
        else:
            fan_type = f"Wow {player}, someone needs to get a building {BUILDING} on campus named after you because of all your impressive UNC sports knowledge!"
    return(fan_type)


if __name__ == "__main__":
    main()