import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    mossleaf = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)

    #      3) Set the pen width to 10
    mossleaf.pensize(width = 10)
    mossleaf.speed(0)
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    chosen_color = simpledialog.askstring(title = "", prompt = "what color would you like the pen to be; blue, red, green, or don't type anything if you want random.")
    colors = ["blue", "red", "green"]
    count = 0
    while count <50:
        circle_size = random.randrange(1, 500)

        if chosen_color == "blue":
            mossleaf.pencolor("blue")
        elif chosen_color == "red":
            mossleaf.pencolor("red")
        elif chosen_color == "green":
            mossleaf.pencolor("green")
        else:
            mossleaf.pencolor(random.choice(colors))
        mossleaf.begin_fill()
        mossleaf.circle(circle_size)
        count += 1

    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
