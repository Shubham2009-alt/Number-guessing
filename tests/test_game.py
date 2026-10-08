import unittest
from unittest.mock import patch

from game import NumberGuessingGame


class TestNumberGuessingGame(unittest.TestCase):
    @patch("game.randint", return_value=50)
    def test_correct_guess(self, _mock_randint):
        game = NumberGuessingGame()

        self.assertEqual(game.guess(50), "correct")
        self.assertEqual(game.attempts, 1)
        self.assertTrue(game.finished)

    @patch("game.randint", return_value=50)
    def test_higher_hint(self, _mock_randint):
        game = NumberGuessingGame()

        self.assertEqual(game.guess(30), "higher")
        self.assertEqual(game.attempts, 1)
        self.assertFalse(game.finished)

    @patch("game.randint", return_value=50)
    def test_lower_hint(self, _mock_randint):
        game = NumberGuessingGame()

        self.assertEqual(game.guess(70), "lower")
        self.assertEqual(game.attempts, 1)

    @patch("game.randint", return_value=50)
    def test_out_of_range_guess(self, _mock_randint):
        game = NumberGuessingGame()

        with self.assertRaises(ValueError):
            game.guess(101)

        self.assertEqual(game.attempts, 0)

    @patch("game.randint", return_value=50)
    def test_finished_game_ignores_new_guess(self, _mock_randint):
        game = NumberGuessingGame()

        game.guess(50)
        self.assertEqual(game.guess(40), "finished")
        self.assertEqual(game.attempts, 1)


if __name__ == "__main__":
    unittest.main()
