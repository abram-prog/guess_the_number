# guess_the_number
# 🎯 Guess the Number (Ultra-Light Python CLI)

A minimal, polished console game in pure Python.  
The computer picks a secret number **1..100**. You have **7 attempts** to guess it.
After each guess you get a hint: **Too low** or **Too high**.

---

## Rules
- Secret number is in the range **1..100**.
- You have **7** attempts.
- Type `q` to quit at any time.
- Guess exactly → you win. Run out of attempts → you lose.

---

## Features
- Clean single-file implementation.
- Robust input handling (numbers only; `q` to quit).
- Clear attempt counter and hints.

---

## Run
```bash
python guess_number.py

# Example:

🎯 Guess the Number 1..100 (q = quit)
[1/7] Your guess (left 7): 50
Too low
[2/7] Your guess (left 6): 75
Too high
[3/7] Your guess (left 5): 63
Too high
[4/7] Your guess (left 4): 58
Too low
[5/7] Your guess (left 3): 60
You goddamn right!!
