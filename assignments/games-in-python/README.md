
# 🎮 Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, and handling user input in Python.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Implement a command-line Hangman game using Python. The program should run from `starter-code.py` in this folder and provide a playable experience in the terminal.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (or `data.csv` if you choose to load words from the CSV).
- Accept single-letter guesses (case-insensitive) and update the displayed progress accordingly (e.g., `_ _ a _ _`).
- Track and display the number of incorrect guesses remaining (suggested default: 6).
- Do not count repeated correct guesses as additional incorrect attempts; repeated incorrect guesses may be counted once.
- End the game when the word is fully guessed or when attempts are exhausted.
- Display a clear win or lose message; on loss reveal the correct word.

### ✨ Optional Enhancements

- Allow whole-word guesses to attempt solving early.
- Show ASCII-art hangman stages for each incorrect guess.
- Load the word list from `data.csv` instead of an in-code list.

#### Example session

```
Word: _ _ _ _ _
Guess: e
Correct! Word: _ e _ _ _
Incorrect guesses left: 6
...
```

Starter code: `starter-code.py` (edit and run from this folder).

Good luck — have fun building and extending the game!
