from turtle import Turtle
from random import randint,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        if randint(1,6)==1:
            new_turtle=Turtle("square")
            new_turtle.shapesize(stretch_wid=1,stretch_len=3)
            new_turtle.color(choice(COLORS))
            new_turtle.penup()
            new_turtle.goto(280,randint(-230,250))
            self.cars.append(new_turtle)
    def move(self):
        for car in self.cars:
            x_cor=car.xcor()-self.move_distance
            car.goto(x_cor,car.ycor())
    def new_level_move(self):
        self.move_distance+=MOVE_INCREMENT


