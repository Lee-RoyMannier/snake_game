# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:07:39 2022

@author: Mannier
"""
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard
import winsound

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        winsound.PlaySound("eat.wav", winsound.SND_ASYNC)
        food.refresh_food()
        snake.extend()
        score_board.add_score()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or (
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):        
        game_on = False
        score_board.game_over()
        
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
            
screen.exitonclick()
snake.done()
