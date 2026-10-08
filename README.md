# Number Guessing Game

A simple Python number guessing game with a clean desktop interface built using **Tkinter**.

The computer chooses a random number between **1 and 100**, and you keep guessing until you find it. After every incorrect guess, the game tells you whether to go higher or lower.

## Features

- Random number from 1–100
- Clean desktop GUI
- Higher/lower hints
- Attempt counter
- Input validation
- New Game button
- Enter-key support
- Separated game logic for easier testing
- Unit tests using Python's built-in unittest
- No third-party packages required

## Preview

The application uses a dark card-style interface with:

- A clear game title
- Large number input
- **Check Guess** action
- **New Game** action
- Live attempt count
- Immediate higher/lower feedback

## Requirements

- Python 3.9 or newer
- Tkinter

Tkinter is included with most standard Python installations. On some Linux distributions, it may need to be installed separately.

## Run the game

Clone the repository:

~~~bash
git clone https://github.com/Shubham2009-alt/Number-guessing.git
cd Number-guessing
~~~

Start the application:

~~~bash
python main.py
~~~

On systems where python points to Python 2, use:

~~~bash
python3 main.py
~~~

## Run the tests

From the repository root:

~~~bash
python -m unittest discover -s tests -v
~~~

## Project structure

~~~text
Number-guessing/
├── main.py                  # Tkinter graphical interface
├── game.py                  # Core game logic
├── tests/
│   └── test_game.py         # Unit tests
├── .github/
│   └── workflows/
│       └── tests.yml        # Automated tests with GitHub Actions
├── .gitignore
└── README.md
~~~

## How the game works

1. A random integer from 1 to 100 is generated.
2. The player enters a guess.
3. The program validates the input.
4. The guess counter increases for valid guesses.
5. The game responds:
   - **Go a little higher** when the guess is too low.
   - **Go a little lower** when the guess is too high.
   - **Correct** when the hidden number is found.
6. A new game can be started at any time.

## Tech stack

- **Python**
- **Tkinter**
- **unittest**
- **GitHub Actions**

## License

This project is available for personal and educational use.
