from turtle import penup, pendown, forward, left, right
from random import randint 

def draw_rectangle(n):
  a = randint(20,200)
  forward(a)
  right(90)
  forward(n)
  right(90)
  forward(a)
  right(90)
  forward(n)
  penup()
  right(180)
  forward(n+10)
  pendown()
  left(90)


penup()
left(180)
forward(150)
right(90)
pendown()
for i in range(20):
  draw_rectangle(15)
