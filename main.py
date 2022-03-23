# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:07:39 2022

@author: Mannier
"""
""" Principal program of the Snake Game
The goal of the file is to split the different elements of the program
into different class in different files.

 __             _            ___                     
/ _\_ __   __ _| | _____    / _ \__ _ _ __ ___   ___ 
\ \| '_ \ / _` | |/ / _ \  / /_\/ _` | '_ ` _ \ / _ \
_\ \ | | | (_| |   <  __/ / /_\\ (_| | | | | | |  __/
\__/_| |_|\__,_|_|\_\___| \____/\__,_|_| |_| |_|\___|

Snake is a video game genre where the player maneuvers a growing line that
becomes a primary obstacle to itself.

The player controls a dot, square, or object on a bordered plane. 
As it moves forward, it leaves a trail behind, resembling a moving snake. 
In some games, the end of the trail is in a fixed position, so the snake 
continually gets longer as it moves. In another common scheme, the snake has 
a specific length, so there is a moving tail a fixed number of units away from 
the head. The player loses when the snake runs into the screen border, 
other obstacle, or itself.

"""
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard
import winsound

# Preparation of the scene
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creation of the pricipals objects
snake = Snake()
food = Food()
score_board = ScoreBoard()

# Keyboard key
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

    # if the snake head is inferior of the distance of the food then the user
    # win one point and the food is another random generate
    if snake.snake_head.distance(food) < 15:
        winsound.PlaySound("eat.wav", winsound.SND_ASYNC)
        food.refresh_food()
        snake.extend()
        score_board.add_score()
        
    # if the head of snake is superior of the distance of the screen then
    # the game is over
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or (
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):        
        game_on = False
        score_board.game_over()
        
    # if the head of the snake touch another snake part then the game is over
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
            
screen.exitonclick()
snake.done()
