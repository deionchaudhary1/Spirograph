"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
t.speed(1000)
t.goto(0,0)

def circle ():
  t.color('#63cff2')
  t.circle(100)
  t.color('#44f255')
  t.circle(84)
def triangle():
  t.color('#9b85d6')
  t.forward(50)
  t.right(45)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(45)
  t.forward(50)
  t.right(45)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(45)
  t.forward(50)
def semi():
  t.color('#de4b02')
  t.circle(100,60)
  t.left(120)
  t.color('#de4b02')
  t.circle(100,60)
n = 0
while n < 36:
  semi()
  circle()
  triangle()
  t.right(10)
  n = n + 1