import random
from turtle import Turtle





def recursive_circles3(turtle, left, right, backward, forward, q, ultra):

    turtle.penup()

    turtle.setpos(-100, -300)

    turtle.pendown()


    for x in range(q):

        my_range = random.randint(1,2)
        pen_rangeR = random.randint(1,255)
        pen_rangeG = random.randint(1,255)
        pen_rangeB = random.randint(1,255)

        turtle.pencolor((pen_rangeR, pen_rangeG, pen_rangeB))

        for i in range(x):

            turtle.forward(forward)

        for i in range(x):

            turtle.backward(backward)

        turtle.left(left)

        turtle.right(right)

        for i in range(x, q):

            if x != 0:

                if x % 10 == 0:

                    turtle.backward(ultra)

def main():
    ANIMATION_SPEED = 0
    leonardo = Turtle()
    leonardo.speed(ANIMATION_SPEED)
    recursive_circles3(leonardo, 1.5, 180, 4, 6, 100, 1)

main()
