import random

secret_number = random.randint(1, 100)

attempts = 5

print("Number Guessing Game")
print("You have only 5 attempts!")
print("Guess the number between 1 and 100")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    attempts -= 1
    print("Remaining attempts:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The correct number was:", secret_number)