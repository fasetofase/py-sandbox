from turtle import *
import time

shape('turtle')

# https://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o5

x = 10
y = 0
while x < 200:
    
    up()
    goto(-y,-y)
    down()
    for _ in range(4):
        forward(x+20)
        left(90)
    x += 20
    y += 10
