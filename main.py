import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.level_number()
    car.create_car()
    car.move()

    if player.ycor()>280:
        player.from_start()
        car.new_level_move()
        score.new_level()
    for each_car in car.cars:
        if player.distance(each_car)<30:
            score.game_over()
            game_is_on=False
screen.exitonclick()
