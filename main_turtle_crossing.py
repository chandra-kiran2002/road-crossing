import time
from turtle import Screen
from turtle import Turtle
from player import Player
from scoreboard import Scoreboard
import scoreboard
from car_manager import CarManager
import random
screen = Screen()
screen.tracer(0)
scoreboard=Scoreboard()

def game():
    screen.setup(width=600, height=600)
    levelBoard=Turtle()
    levelBoard.penup()
    levelBoard.hideturtle()
    levelBoard.goto(-250,270)
    levelBoard.write(f' Level {scoreboard.level}', align="center",
                   font=("Arial", 15, "bold"))
    player = Player()
    car_manager = CarManager()
    car_manager.carSpeed=scoreboard.speed
    game_is_on = True
    screen.listen()
    screen.onkey(player.move_up, "Up")
    while game_is_on:
        time.sleep(0.05)
        screen.update()
        w = random.randint(1, 8)
        if w == 1:
            car_manager.create()
        car_manager.move()
        car_manager.remover()
        # detect collision with car
        f = car_manager.detect(player)
        if f == 1:
            newtim = Turtle()
            newtim.goto(-45,0)
            newtim.write('GAME OVER',move=False, align='left', font=('Arial', 25, 'normal'))
            print('u lost the game')
            time.sleep(2)
            return 0
        if player.ycor() > 280:
            newtim = Turtle()
            newtim.goto(-45, 0)
            newtim.write('YOU WON', move=False, align='left', font=('Arial', 25, 'normal'))
            print("u won the game")
            time.sleep(2)
            return 1
while True:
    if(game()==1):
        scoreboard.increaseLevel()
        screen.clear()
        screen.tracer(0)
        continue
    else:
        break

screen.exitonclick()
