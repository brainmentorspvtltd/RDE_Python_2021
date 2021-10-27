import turtle
import random

t = turtle.Pen()
t.shape("turtle")
colors = ['red','blue','green','black','orange']
t.speed(0)
for i in range(50):
    t.color(random.choice(colors))
    t.circle(5*i)
    t.left(90)
    
