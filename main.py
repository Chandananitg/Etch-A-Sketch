from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")
tim.pensize(2)

def move_fwd():
    tim.forward(10)


def move_back():
    tim.backward(10)


def move_rgt():
    tim.setheading(tim.heading() - 5)


def move_left():
    tim.setheading(tim.heading() + 5)


def clr():
    # screen.clear() - clears everything including all turtles.
    # screen.reset() - for resetting all turtles to initial positions.
    # tim.clear()    - only clears whatever this particular turtle did.
    # tim.setposition(0, 0) - returns to 0,0 coordinates(but draws a line to reach there.
    # tim.home() - brings it back to origin(0,0)

    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(fun=move_fwd, key="Up")
screen.onkeypress(fun=move_back, key="Down")
screen.onkeypress(fun=move_left, key="Left")
screen.onkeypress(fun=move_rgt, key="Right")
screen.onkeypress(fun=clr, key="c")

screen.exitonclick()
