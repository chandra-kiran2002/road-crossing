import time
from turtle import Screen
from turtle import Turtle
from player import Player
from car_manager import CarManager
import random
screen = Screen()
screen.tracer(0)
def game():

    player = Player()
    screen.setup(width=600, height=600)
    car_manager = CarManager()
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
            break
        if player.ycor() > 280:
            newtim = Turtle()
            newtim.goto(-45, 0)
            newtim.write('YOU WON', move=False, align='left', font=('Arial', 25, 'normal'))
            print("u won the game")
            break
game()
screen.exitonclick()
