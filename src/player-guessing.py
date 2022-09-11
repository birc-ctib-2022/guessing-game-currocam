# The following code is just to setup the exercise.
# You do not need to understand but can jump to the game below.

from random import randint


def input_integer(prompt: str) -> int:
    """Get an integer from the user."""
    while True:
        try:
            inp = input(prompt)
            i = int(inp)
            return i
        except ValueError:
            print(inp, "is not a valid integer.")


# Here is an implementation of the game. The computer picks
# a number and you should try to guess it.

# When picking a random number, we specify the interval
# [low,high). Since high is not included in the interval,
# we need to use 1 to 21 to get a random number in the
# interval [1,20].
true_val = randint(1, 21)

# Now, repeat guessing until we get the right number.
guess = input_integer("Make a guess> ")
while guess != true_val:
    if guess > true_val:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = input_integer("Make a guess> ")
print("You got it!")
