import turtle

from itertools import cycle
colors = cycle(['Goldenrod', 'Purple', 'Lawn Green', 'Seashell', 'Light blue', 'yellow'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+7, angle+4,shift+3)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(40,3,5)
