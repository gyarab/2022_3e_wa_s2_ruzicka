import random
from turtle import *
import math

def domecek(a):
    left(90)
    forward(a)
    right(90)
    forward(a)
    right(45 + 90)
    forward(math.sqrt(a**2 * 2))
    left(45 + 90)
    forward(a)
    left(90)
    forward(a)
    left(45)
    forward(math.sqrt(a**2 / 2) / 4)

    right(45)
    forward(a/4)
    right(90)
    forward(a/16)
    left(90)
    forward(a/12)
    left(90)
    forward(a/16 * 2 + math.cos(math.pi/4)*(math.sqrt(a**2 / 2) / 4))
    left(90)
    forward(a/12)
    left(90)
    forward(a/16)
    right(90)
    forward(a/4 - math.sin(math.pi/4)*(math.sqrt(a**2 / 2) / 4))
    right(45 + 90)

    forward(math.sqrt(a**2 / 2) / 2)
    left(90)
    forward(math.sqrt(a**2 * 2) / 2)
    left(90)
    forward(math.sqrt(a**2 * 2))
    left(45)

goto(-400, 0)
for i in range(12):
    domecek(random.randint(30, 150))
    forward(20)


exitonclick()