"""Core logic for the Number Guessing game."""

from random import randint


class NumberGuessingGame:
    """Manage one game of guessing a number from 1 to 100."""

    MIN_NUMBER = 1
    MAX_NUMBER = 100

    def __init__(self):
        self.reset()

    def reset(self):
        """Start a new game with a new secret number."""
        self.secret_number = randint(self.MIN_NUMBER, self.MAX_NUMBER)
        self.attempts = 0
        self.finished = False

    def guess(self, number):
        """Evaluate a guess and return higher, lower, or correct."""
        if not self.MIN_NUMBER <= number <= self.MAX_NUMBER:
            raise ValueError(
                f"Enter a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}."
            )

        if self.finished:
            return "finished"

        self.attempts += 1

        if number == self.secret_number:
            self.finished = True
            return "correct"

        return "higher" if number < self.secret_number else "lower"
