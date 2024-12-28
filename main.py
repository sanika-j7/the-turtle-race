from turtle import Turtle, Screen
import random
import time

# Initialize game variables
is_race_on=False
screen=Screen()
screen.setup(width=600,height=500)

# Set the background color and title
screen.bgcolor("lightblue")
screen.title("Turtle Race Game!")

# User bet input
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

# List of turtle colors and initial positions
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

# Create 6 turtles
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start race if user has placed a bet
if user_bet:
    is_race_on=True

# Main race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has won (crossed the finish line)
        if turtle.xcor()>230:
            is_race_on=False  # End the race
            winning_color=turtle.pencolor()

            # Display result in the console
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            # Display winner text on screen
            winner_text=Turtle()
            winner_text.hideturtle()
            winner_text.penup()
            winner_text.goto(0,150)
            winner_text.color(winning_color)
            winner_text.write(f"The {winning_color} turtle wins!",align="center",font=("Arial",24,"bold"))
            time.sleep(2)  # Pause for 2 seconds to let the user see the winner

            break  # Exit the loop after a winner is found

        # Make each turtle move a random amount
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

    # Optional: Speed the race up by sleeping less
    time.sleep(0.05)

# Wait for user to click before closing the window
screen.exitonclick()
