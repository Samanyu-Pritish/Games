import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Shape Shooter")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Player shape
player = turtle.Turtle()
player.shape("triangle")
player.color("green")
player.penup()
player.goto(0, -250)
player.setheading(90)  # Point upwards
player.speed(0)

# Bullet shape
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("red")
bullet.penup()
bullet.goto(0, -240)  # Start just above the player
bullet.hideturtle()
bullet.speed(0)
bullet_state = "ready"  # "ready" means you can't see the bullet

# Target shape
target = turtle.Turtle()
target.shape("square")
target.color("yellow")
target.penup()
target.speed(0)
target.goto(random.randint(-380, 380), random.randint(100, 250))

# Score variables
score = 0

# Functions to move the player
def player_left():
    x = player.xcor()
    x -= 20
    if x < -390:
        x = -390
    player.setx(x)

def player_right():
    x = player.xcor()
    x += 20
    if x > 390:
        x = 390
    player.setx(x)

# Function to shoot
def shoot():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)  # Position bullet above player
        bullet.showturtle()

# Check for collision
def is_collision(target, bullet):
    if bullet.distance(target) < 20:  # Adjust the value for collision detection
        return True
    return False

# Keyboard bindings
wn.listen()
wn.onkeypress(player_left, "Left")
wn.onkeypress(player_right, "Right")
wn.onkeypress(shoot, "space")

# Main game loop
while True:
    wn.update()

    # Move the bullet
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + 20)

    # Check if bullet has gone out of bounds
    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet_state = "ready"

    # Check for collision with target
    if is_collision(target, bullet):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.goto(0, -240)  # Reset bullet position
        score += 10
        print(f"Score: {score}")
        target.goto(random.randint(-380, 380), random.randint(100, 250))  # Move target to a new location

# Close the game when the window is clicked
wn.mainloop()