import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
t = turtle.Turtle()
t.speed(0)

# --- Draw face (yellow circle) ---
t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# --- Left eye ---
t.penup()
t.goto(-35, 35)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# --- Right eye ---
t.penup()
t.goto(35, 35)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# --- Smile ---
t.penup()
t.goto(-50, 0)
t.setheading(-60)  # tilt for arc
t.pendown()
t.width(4)
t.circle(60, 120)  # radius, angle

# Finish
t.hideturtle()
turtle.done()
