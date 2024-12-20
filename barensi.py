import turtle as t
import random

n=10000
x,y=.5,0
t.speed(1000)


for i in range(n):
    r=random.randrange(0,101)
    if 0<=r<2: v=0
    if 3<=r<18: v=1
    if 18<=r<31: v=2
    if 31<=r<101: v=3

    cx=[0.50,((-0.14*x)+(0.26*y)+0.57),((0.17*x)-(0.21*y)+0.41),((0.78*x)+(0.03*y)+0.11)]
    cy=[(0.27*y),((0.25*x)+(0.22*y)-0.04),((0.22*x)+(0.18*y)+0.09),((-0.03*x)+(0.74*y)+0.27)]
    x=(cx[v])
    y=(cy[v])
    t.penup()
    t.goto(300*x,300*y)
    t.dot(3,"green")



t.done()