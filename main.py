import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Control
screen.listen()
screen.onkey(player.up, "Up")

#Game
game_is_on = True
loop_number = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #car_manager.create_car()

    #Create & move cars
    trigger = loop_number % 6
    if trigger == 0:
        car_manager.create_car()

    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect turtle at finish line
    if player.ycor() >= 280:
        print("Error")
        player.starting_position()
        car_manager.faster()
        scoreboard.level_up()

    loop_number += 1



screen.exitonclick()