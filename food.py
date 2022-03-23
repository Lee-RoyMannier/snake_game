# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:49:55 2022

@author: Mannier
"""
"""
Class of the food for the snake game.
Here the program generate a food in random screen
"""
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.penup()
       self.shapesize(0.5, 0.5)
       self.color("blue")
       self.speed("fastest")
       self.refresh_food()
       
       
    def refresh_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)