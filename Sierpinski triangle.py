# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:52:12 2022

@author: Ricky Wiggins Jr
"""

import turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.backward(200)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()

t.setheading(180)
t.color("white", "#800020")
t.begin_fill()
t.right(90)
t.forward(350)
t.right(90)
t.forward(400)
t.right(90)
t.forward(350)
t.right(90)
t.forward(400)
t.end_fill()



def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):       
        t.rt(120)          
        t.fd(length)
        num = 0
        num += 1
        if num % 2 == 1:
          t.color("black", "red")
          t.begin_fill()
    t.end_fill()

def sierpinski_order_n_recursive(n , length):
    if n == 1:
        draw_triangle(length)
    else:
        sierpinski_order_n_recursive(n - 1, length)
        t.rt(120)
        t.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n -1, length)
        t.lt(120)
        t.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n - 1, length)
        t.fd(length * 2 ** (n - 2))
        
sierpinski_order_n_recursive(4, 50)