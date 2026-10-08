# Number Guessing Game

A small number guessing game available as both a **Python desktop app** and a **browser game**. The player tries to find a randomly generated number between 1 and 100 while receiving higher/lower hints.

The computer chooses a random number between **1 and 100**, and you keep guessing until you find it. After every incorrect guess, the game tells you whether to go higher or lower.

## Features

- Random number from 1–100
- Responsive browser UI
- Python/Tkinter desktop UI
- Higher/lower hints
- Attempt counter
- Best-score tracking in the browser using localStorage
- Input validation
- New Game button
- Enter-key support
- Separated Python game logic for easier testing
- Unit tests using Python's built-in unittest
- GitHub Actions automation
- GitHub Pages deployment

## Preview

The application uses a dark card-style interface with:

- A clear game title
- Large number input
- **Check Guess** action
- **New Game** action
- Live attempt count
- Immediate higher/lower feedback

## Browser version

The browser version is made with plain HTML, CSS, and JavaScript, so it requires no build step or third-party packages.

### GitHub Pages

The repository includes a GitHub Pages workflow. Before the first deployment, enable **Settings → Pages → Build and deployment → Source: GitHub Actions** in the repository. The workflow detects whether Pages is enabled and skips deployment cleanly when it is not.

## Desktop requirements

- Python 3.9 or newer
- Tkinter

Tkinter is included with most standard Python installations. On some Linux distributions, it may need to be installed separately.

## Run the desktop game

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
├── index.html               # Browser game page
├── style.css                # Browser game styling
├── script.js                # Browser game logic
├── main.py                  # Tkinter desktop interface
├── game.py                  # Python game logic
├── tests/
│   └── test_game.py         # Unit tests
├── .github/
│   └── workflows/
│       ├── tests.yml        # Automated Python tests
│       └── pages.yml        # GitHub Pages deployment
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

- **HTML5**
- **CSS3**
- **JavaScript**
- **Python**
- **Tkinter**
- **unittest**
- **GitHub Actions**
- **GitHub Pages**

## License

No explicit open-source license has been added to this repository yet.
