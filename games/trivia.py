import random

# Define the questions and answers
questions = [
    {
        "question": "What shape has three sides?",
        "options": ["Triangle", "Circle", "Square", "Rectangle"],
        "correct_answer": "Triangle"
    },
    {
        "question": "What shape has four equal sides?",
        "options": ["Circle", "Triangle", "Square", "Pentagon"],
        "correct_answer": "Square"
    },
    {
        "question": "What is the shape of the earth?",
        "options": ["Flat", "Square", "Triangle", "Sphere"],
        "correct_answer": "Sphere"
    },
    {
        "question": "What shape has four sides but is not a square?",
        "options": ["Square", "Rectangle", "Circle", "Triangle"],
        "correct_answer": "Rectangle"
    },
    {
        "question": "What is a 3D shape that has 6 rectangular faces?",
        "options": ["Cube", "Sphere", "Cylinder", "Rectangular Prism"],
        "correct_answer": "Rectangular Prism"
    },
    {
        "question": "How many vertices does Cube has?",
        "options": ["10", "12", "6", "8"],
        "correct_answer": "8"
    },
    {
        "question": "Where is the longest river in the world located?",
        "options": ["Antarctica", "Africa", "Europe", "Asia"],
        "correct_answer": "Africa"
    },
    {
        "question": "Which is the largest Flower in the world?",
        "options": ["Sunflower", "Lotus", "Amazon Lily", "Rafflesia Alnordi"],
        "correct_answer": "Africa"
    },
]

# Function to display the question and options and get user input
def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                return question["options"][answer - 1]
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to run the trivia game
def run_trivia():
    score = 0
    random.shuffle(questions)  # Shuffle questions for randomness

    for question in questions:
        user_answer = ask_question(question)
        if user_answer == question["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['correct_answer']}\n")

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")

# Main function to start the trivia game
if __name__ == "__main__":
    print("Welcome to the Shape Trivia Game!")
    run_trivia()