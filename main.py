import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.delay(0)

player = Player()
screen.onkeypress(player.move, "Up")

scoreboard = Scoreboard()

car = CarManager()
cars = [car]
level = 0
step = 1
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if step % 3 == 0:
        new_car = CarManager()
        cars.append(new_car)
    step += 1

    car_positions = []
    for car in cars:
        car.move(level)
        if player.distance(car.position()) < 20:
            scoreboard.game_over()
            game_is_on = False
            pass
        elif car.xcor() < -301:
            cars.remove(car)

    if player.ycor() > 280:
        player.position_zero()
        level += 1
        scoreboard.update_score(level + 1)

screen.exitonclick()
