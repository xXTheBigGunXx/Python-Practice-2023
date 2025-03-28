import turtle
from time import sleep
import math
screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed(20)
def plate():
    turtle.pensize(2)
    turtle.color("white")
    turtle.begin_fill()
    turtle.right(0)
    turtle.forward(900)
    turtle.penup()
    turtle.goto(0,450)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(450)
    turtle.penup()
    turtle.goto(-900,0)
    turtle.pendown()
    turtle.right(-90)
    turtle.forward(900)
    turtle.penup()
    turtle.goto(0,-450)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(450)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

plate()
turtle.speed(1)
r = 1
x = 1
y = 1
turtle.circle(r, 90)
for _ in range(1, 14):
    turtle.circle(r, 90)
    r = x+y
    x=y
    y=r
    print(r, x, y)

sleep(5)
turtle.done()