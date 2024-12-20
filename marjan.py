import turtle as t
import random


n=9000
x,y=.5,0
t.speed(10000)


for i in range(n):
    r=random.randrange(0,101)
    if 0<=r<41: r=0
    if 41<=r<56: r=1
    if 56<=r<101: r=2
    cx=[((0.31*x)-(0.53*y)+0.89),((0.31*x)-(0.08*y)+0.22),((0.55*y)+0.01)]
    cy=[((-0.46*x)-(0.29*y)+1.04),((0.15*x)-(0.45*y)+0.34),((0.69*x)-(0.20*y)+0.38)]
    x=(cx[r])
    y=(cy[r])
    t.penup()
    t.goto(300*x,300*y)
    t.dot(5,'black')


t.done()
