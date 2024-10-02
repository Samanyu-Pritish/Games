import random
secret_number = random.randint(1, 100)
guess = 0
chances = 5
while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("high, try again.")
        chances -= 1
    elif guess < secret_number:
        print("Too, try again.")
        chances -= 1
    elif guess == secret_number:
        print("You guessed it right. The number was", secret_number)
        exit()
    elif chances == 0:
        print("You lose. The number was", secret_number)
        exit()