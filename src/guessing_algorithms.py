from abc import ABC, abstractmethod
from statistics import mean


class GuessingAlgorithm(ABC):
    def __init__(self, min_int, max_int):
        self.min_int: int = min_int
        self.max_int: int = max_int

    @abstractmethod
    def guess(self):
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
