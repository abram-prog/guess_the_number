import random

secret = random.randint(1, 100)
attempts = 7
print("Guess the Number 1..100 (q = quit)")

for i in range(1, attempts + 1):
    tries_left = attempts - i + 1
    raw = input(f"[{i}/{attempts}] Your guess (left {tries_left}): ").strip()
    if raw.lower() in {"q", "quit", "exit"}:
        print("Bye!")
        break
    try:
        g = int(raw)
    except ValueError:
        print("Number, please.")
        continue

    if g == secret:
        print("You goddamn right!!")
        break
    print("Too low" if g < secret else "Too high")
else:
    print(f"You lost. The right answer is {secret}")
