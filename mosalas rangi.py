import turtle as t
import random
n=6000
cx=[-0.5,0.5,0.0]
cy=[-0.5,-0.5,0.366]
x,y=0,0
t.speed(10)
for i in range(n):
    r=random.randrange(0,3)
    x=(x+cx[r])/2
    y=(y+cy[r])/2
    t.penup()
    t.goto(400*x,400*y)
    if y>-0.067 :
      t.dot(5,"blue")
    else:
        if x>0.0 :
            t.dot(5,"green")
        else:
            t.dot(5,"red")
t.done()
