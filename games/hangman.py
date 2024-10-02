import random

def choose_word():
    word_pool = ["python", "hangman", "programming", "function", "variable", "speed", "graphics"]
    return random.choice(word_pool)

def display_board(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        print("Word to guess:", display_board(word, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
            
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
            
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The correct word was: {word}")

if __name__ == "__main__":
    hangman()