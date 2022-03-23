# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:22:21 2022

@author: Mannier
"""
"""
Class create scoreboard and update score if the snake eat food
"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:   
            self.high_score = int(file.read())
            
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", 
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
