import random
from turtle import Turtle





def recursive_circles3(turtle, left, right, backward, forward, q, ultra):

    colors = ["blue", "red", "green", "black"]
    
    turtle.color(random.choice(colors))


    for x in range(q):

        turtle.color(random.choice(colors))

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
    recursive_circles3(leonardo, 90, 45, 5, 6, 100, 2)

main()
