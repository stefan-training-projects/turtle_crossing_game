import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_car()

    #player reached finish line
    if player.ycor() == 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_car_speed()
    #collision with car
    for car in car_manager.cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
