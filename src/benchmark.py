from hashlib import algorithms_available
from random import randint
from statistics import mean


from guessing_algorithms import GuessingAlgorithm, GuessingBottomUp, GuessingMiddleUpOrDown, GuessingRandom, GuessingUpBottom, ValueNotInRangeError


def give_feedback(guess: int, correct_value: int):
    if correct_value > guess:
        return 'low'
    elif correct_value < guess:
        return 'high'
    else:
        return 'hit'


def run_non_interactive_prompt(algorithm: GuessingAlgorithm, min_int: int, max_int: int, correct_value: int) -> int:
    guesser = algorithm(min_int, max_int)
    counter = 0
    while True:
        counter += 1
        # First, get next guess value
        guess = guesser.guess()
        result = give_feedback(guess, correct_value)
        if result == "hit":
            break
        # Try to get feedback (if GuessingMiddleUpOrDown algorithm)
        try:
            guesser.get_feedback(result, guess)
        except:
            continue
    return counter


def main():
    algorithms = [GuessingBottomUp, GuessingMiddleUpOrDown,
                  GuessingRandom, GuessingUpBottom]
    min_value, max_value = 1, 10000
    actual_values = [randint(min_value, max_value) for _ in range(500)]
    for algorithm in algorithms:
        print(algorithm.__name__)
        n_tries = list(map(lambda x: run_non_interactive_prompt(
            algorithm, min_value, max_value, x), actual_values))
        print(mean(n_tries))


if __name__ == "__main__":
    main()
