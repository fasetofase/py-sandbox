from turtle import *
import time

shape('turtle')

# https://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o5

x = 3
y = 0
while x < 10:
    
    up()
    goto(-y,-y)
    down()
    for _ in range(x):
        forward(x*5+20)
        left((180-180*((x-2)/x)))
    x += 1
    y += x**0.5