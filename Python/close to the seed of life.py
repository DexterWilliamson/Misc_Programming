import random
from turtle import Turtle

def recursive_circles3(turtle, left, right, backward, forward, q, ultra, ultra2):

    colors = ["black"]
    
    turtle.color(random.choice(colors))


    for x in range(q):

        turtle.circle(75)

        turtle.color(random.choice(colors))

        for i in range(x):

            turtle.forward(forward)

        for i in range(x):

            turtle.backward(backward)

        turtle.left(left)

        turtle.right(right)

        #for i in range(x, q):

            #if x != 0:

                #if x % 10 == 0:

                    #turtle.backward(ultra)

    turtle.penup()

    turtle.setpos(-3,-156)

    turtle.pendown()

    turtle.circle(153)
                

def main():
    ANIMATION_SPEED = 0
    leonardo = Turtle()
    leonardo.speed(ANIMATION_SPEED)
    recursive_circles3(leonardo, 0, 60, 5, 6, 6, 2, 2)

main()
