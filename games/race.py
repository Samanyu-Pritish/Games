import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Shape Race")
screen.setup(width=800, height=600)

# Function to create a turtle
def create_turtle(color, y_position):
    new_turtle = turtle.Turtle()
    new_turtle.color(color)
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(-380, y_position)
    return new_turtle

# Create turtles
colors = ["red", "blue", "green", "yellow"]
turtles = []

for i in range(len(colors)):
    t = create_turtle(colors[i], -200 + i * 50)
    turtles.append(t)

# Get user bet
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? (red, blue, green, yellow):")

# Start the race
def race():
    race_on = True
    while race_on:
        for t in turtles:
            distance = random.randint(1, 10)
            t.forward(distance)

            # Check for a winner
            if t.xcor() > 380:
                race_on = False
                winner = t.pencolor()
                if winner == user_bet:
                    print(f"You won! The {winner} turtle is the winner!")
                else:
                    print(f"You lost! The {winner} turtle is the winner!")

race()

# Finish the game
screen.exitonclick()