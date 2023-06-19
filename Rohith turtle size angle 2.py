import turtle

from itertools import cycle
colors = cycle(['red','orange','yellow','green','blue','purple',])

def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+3,angle-15,shift+2)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(30,0,1)
