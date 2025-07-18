import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# Move the turtle with a key press
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create the cars and move the cars
    car_manager.create_car()
    car_manager.move_cars()
    # Detect collision with the car


    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when turtle reaches the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    # Create a score board


screen.exitonclick()
