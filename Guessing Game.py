secret_number = 42

for attempt in range(1, 6):
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Invalid number! Try again.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Wrong guess! Attempts left:", 5 - attempt)
else:
    print("Game Over! You lost.")