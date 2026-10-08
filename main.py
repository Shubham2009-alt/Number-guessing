"""Graphical interface for the Number Guessing game."""

import tkinter as tk
from tkinter import messagebox, ttk

from game import NumberGuessingGame


class NumberGuessingApp(tk.Tk):
    """Desktop UI for the Number Guessing game."""

    def __init__(self):
        super().__init__()

        self.game = NumberGuessingGame()
        self.title("Number Guessing Game")
        self.geometry("520x620")
        self.minsize(460, 560)
        self.configure(bg="#0f172a")

        self._build_style()
        self._build_ui()
        self._update_stats()

        self.bind("<Return>", lambda _event: self.check_guess())
        self.guess_entry.focus_set()

    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Card.TFrame",
            background="#1e293b",
        )
        style.configure(
            "Title.TLabel",
            background="#1e293b",
            foreground="#f8fafc",
            font=("Segoe UI", 26, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background="#1e293b",
            foreground="#94a3b8",
            font=("Segoe UI", 11),
        )
        style.configure(
            "Stat.TLabel",
            background="#334155",
            foreground="#f8fafc",
            font=("Segoe UI", 11, "bold"),
            padding=(12, 8),
        )
        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=(18, 11),
        )
        style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10),
            padding=(14, 9),
        )

    def _build_ui(self):
        outer = ttk.Frame(self, style="Card.TFrame", padding=36)
        outer.pack(fill="both", expand=True, padx=28, pady=28)

        ttk.Label(outer, text="Number Guessing", style="Title.TLabel").pack(
            pady=(18, 6)
        )
        ttk.Label(
            outer,
            text="Find the hidden number between 1 and 100.",
            style="Subtitle.TLabel",
        ).pack(pady=(0, 30))

        self.status_var = tk.StringVar(value="Make your first guess.")
        tk.Label(
            outer,
            textvariable=self.status_var,
            bg="#1e293b",
            fg="#38bdf8",
            font=("Segoe UI", 15, "bold"),
            wraplength=390,
            height=3,
        ).pack(fill="x", pady=(0, 20))

        self.guess_var = tk.StringVar()
        self.guess_entry = ttk.Entry(
            outer,
            textvariable=self.guess_var,
            justify="center",
            font=("Segoe UI", 20),
            width=12,
        )
        self.guess_entry.pack(ipady=8, pady=(0, 14))

        ttk.Button(
            outer,
            text="Check Guess",
            style="Primary.TButton",
            command=self.check_guess,
        ).pack(fill="x", pady=(0, 10))

        ttk.Button(
            outer,
            text="New Game",
            style="Secondary.TButton",
            command=self.new_game,
        ).pack(fill="x")

        stats = ttk.Frame(outer, style="Card.TFrame")
        stats.pack(fill="x", pady=(30, 0))

        self.attempts_var = tk.StringVar()
        self.best_var = tk.StringVar(value="Best: —")

        ttk.Label(stats, textvariable=self.attempts_var, style="Stat.TLabel").pack(
            side="left", expand=True, fill="x", padx=(0, 5)
        )
        ttk.Label(stats, textvariable=self.best_var, style="Stat.TLabel").pack(
            side="left", expand=True, fill="x", padx=(5, 0)
        )

        tk.Label(
            outer,
            text="Tip: Press Enter to submit a guess.",
            bg="#1e293b",
            fg="#64748b",
            font=("Segoe UI", 9),
        ).pack(pady=(26, 0))

    def _update_stats(self):
        self.attempts_var.set(f"Attempts: {self.game.attempts}")

    def check_guess(self):
        value = self.guess_var.get().strip()

        if not value:
            self.status_var.set("Enter a number first.")
            self.guess_entry.focus_set()
            return

        try:
            guess = int(value)
        except ValueError:
            self.status_var.set("That is not a valid integer. Try again.")
            self.guess_entry.select_range(0, tk.END)
            self.guess_entry.focus_set()
            return

        try:
            result = self.game.guess(guess)
        except ValueError as error:
            self.status_var.set(str(error))
            self.guess_entry.select_range(0, tk.END)
            self.guess_entry.focus_set()
            return

        self._update_stats()

        if result == "higher":
            self.status_var.set("Go a little higher.")
        elif result == "lower":
            self.status_var.set("Go a little lower.")
        elif result == "correct":
            self.status_var.set(
                f"Correct! You found it in {self.game.attempts} "
                f"attempt{'s' if self.game.attempts != 1 else ''}."
            )
            self.best_var.set(f"Best: {self.game.attempts}")
            messagebox.showinfo(
                "You got it!",
                f"The number was {self.game.secret_number}.\n"
                f"You needed {self.game.attempts} guesses.",
            )
            self.guess_entry.config(state="disabled")
        elif result == "finished":
            self.status_var.set("This round is over. Start a new game.")

        self.guess_entry.select_range(0, tk.END)
        self.guess_entry.focus_set()

    def new_game(self):
        self.game.reset()
        self.guess_entry.config(state="normal")
        self.guess_var.set("")
        self.status_var.set("New number generated. Make your first guess.")
        self._update_stats()
        self.guess_entry.focus_set()


if __name__ == "__main__":
    app = NumberGuessingApp()
    app.mainloop()
