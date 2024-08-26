import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Instantiating objectes
player = Player()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
loop_count = 0
car_manager = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    loop_count += 1
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.finish():
        player.go_back()
        car_manager.increase_speed()
        scoreboard.increase_level()




screen.exitonclick()
