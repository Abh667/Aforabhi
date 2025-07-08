import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen().bgcolor('yellow')
t.speed(100)
n=100
h=100
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(5):
        t.left(2)
        t.circle(100)