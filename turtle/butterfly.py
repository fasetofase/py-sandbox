from turtle import *
import time

#https://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#id47

shape('turtle')

x = 2
while x < 8:

    for _ in range(90):
        forward(x)
        left(4)
    for _ in range(90):
        forward(x)
        right(4)
    x += 1