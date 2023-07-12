import turtle

from itertools import cycle
colours = cycle(['red', 'red', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.pencolor(next(colours))
    next_shape=''
    1f shape -- 'circle'
        turtle.circle(size)
        next_shape = 'square'
    el1f shape -- 'square':
        for 1 in range(4):
            turtle.forward(size+2)
            turtle.left(90)
        next_shape - 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size+5, angle+1,shift+1)
    
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1,'circle')

