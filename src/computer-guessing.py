# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.

from guessing_algorithms import GuessingAlgorithm, GuessingBottomUp, GuessingMiddleUpOrDown, GuessingRandom, GuessingUpBottom, ValueNotInRangeError


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


def run_interactive_prompt(algorithm: GuessingAlgorithm, min_int: int, max_int: int):
    # Print info
    print(
        f"Please thing of a number from {min_int} to {max_int}, both included.")
    print("Let me know how good my guess is.\n")
    guesser = algorithm(min_int, max_int)
    while True:
        # First, get next guess value
        try:
            guess = guesser.guess()
        except ValueNotInRangeError:
            print('No correct value in the indicated range')
            break
        # Then, check it
        result = input_selection(
            f"I'm guessing {guess}\nHow is my guess?",
            ["low", "hit", "high"]
        )
        if result == "hit":
            print("Wuhuu!")
            break
        # Try to get feedback (if GuessingMiddleUpOrDown algorithm)
        try:
            guesser.get_feedback(result, guess)
        except ValueNotInRangeError:
            print('No correct value in the indicated range')
            break
        except:
            continue


def main():
    user_algorithm = input_selection(
        "Now, you should select one of the available algorithms",
        ['BottomUp', 'pBottom', 'MiddleUpOrDown', 'Random']
    )
    match user_algorithm:
        case "BottomUp": run_interactive_prompt(GuessingBottomUp, 1, 20)
        case "UpBottom": run_interactive_prompt(GuessingUpBottom, 1, 20)
        case "MiddleUpOrDown": run_interactive_prompt(GuessingMiddleUpOrDown, 1, 20)
        case "Random": run_interactive_prompt(GuessingRandom, 1, 20)


if __name__ == "__main__":
    main()
