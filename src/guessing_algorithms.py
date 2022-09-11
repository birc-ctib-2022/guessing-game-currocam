from abc import ABC, abstractmethod
from random import randint
from statistics import mean


class GuessingAlgorithm(ABC):
    def __init__(self, min_int, max_int):
        self.min_int: int = min_int
        self.max_int: int = max_int

    @abstractmethod
    def guess(self) -> int:
        pass


class ValueNotInRangeError(Exception):
    """Raised when the correct value is not in the given range"""
    pass


class GuessingBottomUp(GuessingAlgorithm):
    def guess(self):
        guess = self.min_int
        if guess <= self.max_int:
            self.min_int += 1
            return guess
        else:
            raise ValueNotInRangeError()


class GuessingUpBottom(GuessingAlgorithm):
    def guess(self):
        guess = self.max_int
        if guess >= self.min_int:
            self.max_int -= 1
            return guess
        else:
            raise ValueNotInRangeError()


class GuessingMiddleUpOrDown(GuessingAlgorithm):
    def get_feedback(self, answer: str, guess: int):
        if self.min_int == self.max_int:
            raise ValueNotInRangeError()
        match answer:
            case "low":
                self.min_int = guess + 1
            case "high":
                self.max_int = guess - 1

    def guess(self):
        return round(mean([self.min_int, self.max_int]))


class GuessingRandom(GuessingAlgorithm):
    def __init__(self, min_int, max_int):
        super().__init__(min_int, max_int)
        self.previous_attempts = set()

    def get_feedback(self, answer: str, guess: int):
        self.previous_attempts.add(guess)

    def guess(self):
        if len(self.previous_attempts) == self.max_int - self.min_int + 1:
            raise ValueNotInRangeError()
        while True:
            guess = randint(self.min_int, self.max_int)
            if guess not in self.previous_attempts:
                break
        return guess
