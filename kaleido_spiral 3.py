import turtle

from itertools import cycle
colors = cycle(['red', 'grey', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.bgcolor('white')
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+10, angle+10,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)
