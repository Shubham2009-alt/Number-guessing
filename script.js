const MIN = 1;
const MAX = 100;

let secretNumber;
let attempts = 0;
let bestScore = Number(localStorage.getItem("numberGuessingBest")) || null;
let finished = false;

const form = document.querySelector("#guess-form");
const input = document.querySelector("#guess");
const status = document.querySelector("#status");
const attemptsElement = document.querySelector("#attempts");
const bestElement = document.querySelector("#best");
const newGameButton = document.querySelector("#new-game");

function startGame() {
  secretNumber = Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;
  attempts = 0;
  finished = false;
  input.disabled = false;
  form.querySelector("button").disabled = false;
  input.value = "";
  status.textContent = "Make your first guess.";
  updateStats();
  input.focus();
}

function updateStats() {
  attemptsElement.textContent = attempts;
  bestElement.textContent = bestScore ?? "—";
}

function showMessage(message) {
  status.textContent = message;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  if (finished) {
    showMessage("This round is over. Start a new game.");
    return;
  }

  const guess = Number(input.value);

  if (!Number.isInteger(guess) || guess < MIN || guess > MAX) {
    showMessage("Enter a whole number between 1 and 100.");
    input.select();
    return;
  }

  attempts += 1;

  if (guess < secretNumber) {
    showMessage("Go a little higher.");
  } else if (guess > secretNumber) {
    showMessage("Go a little lower.");
  } else {
    finished = true;
    input.disabled = true;
    form.querySelector("button").disabled = true;

    if (bestScore === null || attempts < bestScore) {
      bestScore = attempts;
      localStorage.setItem("numberGuessingBest", String(bestScore));
      showMessage(`Correct! New best score: ${attempts} attempt${attempts === 1 ? "" : "s"}.`);
    } else {
      showMessage(`Correct! You found it in ${attempts} attempt${attempts === 1 ? "" : "s"}.`);
    }
  }

  updateStats();
  input.select();
});

newGameButton.addEventListener("click", startGame);

startGame();
