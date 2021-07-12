#It was done for class using resources provided by the instructor.
import turtle
def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:# The base case is just a straight line
        t.forward(size)
    else:
         koch(t, order-1, size/2) # Go 1/3 of the way
         t.left(60)
         koch(t, order-1, size/2)
         t.right(120)
         koch(t, order-1, size/2)
         t.left(60)
         koch(t, order-1, size/2)

def main():
    size=300
    screen=turtle.Screen()
    screen.setup(size+20,size+20)#window space
    screen.screensize(size,size)#drawing space
    screen.bgcolor("green")

    turtle.color("blue")
    turtle.speed(50)
    turtle.penup()
    turtle.goto(-size/4,size/4)
    turtle.pendown()
    for i in range(3):
          koch(turtle,2,70)
          turtle.right(120)
    turtle.hideturtle()
    screen.exitonclick()# I kept the exitonclick to check the cursor disapper.

if __name__ == '__main__':
    main()
