import turtle as tr
from time import sleep

tr.penup()
tr.goto(0, -100)
tr.pendown()
tr.circle(100)
tr.right(225)
for _ in range(8):
    tr.goto(0, 0)
    tr.right(45)
    tr.forward(184.775906)
    tr.right(157.5)
    tr.forward(100)
    tr.back(100)
    tr.right(202.5)
    tr.right(82.5)
    tr.forward(30)
    tr.right(150)
    tr.forward(30)
    tr.left(75)
    tr.forward(84.470587)
    tr.right(112.5)
    tr.forward(76.536686)
    tr.right(112.5)
    tr.forward(84.470587)
    tr.left(75)
    tr.forward(30)
    tr.right(150)
    tr.forward(30)
    tr.left(97.5)
    sleep(2)

sleep(500)



