import turtle

from itertools import cycle
colors = cycle(['red', 'maroon', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.bgcolor('white')
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle-20,shift-10)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)
