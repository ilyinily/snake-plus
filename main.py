from turtle import Screen
import snake
import food
import time
import scoreboard
# Done 1: Create the snake itself
# Done 2: Make the snake movable
# Done 3: Make the food - Can also make the food movable, too!
# Done 4: Make the food collision working
# Done 5: Make the scoreboard
# Todo 6: End game by hitting the wall
# Todo 7: End game by hitting the snake's tail
# Todo 8: Detect collisions of multiple snakes (2 for convenience)
# Done 9: Introduce leveling of game speed
# Todo 10: Make the snake a series of turtles following the leader. Not food but other turtles which join the cause.
# Todo 10.1: It is also possible that extra turtles need to be combined in color, especially good for multiplayer.
# Todo 11: In Multiplayer game, it is useful to collect joint score - and maybe record the joint result.

X_SIZE = 1200
Y_SIZE = 600

# Setting up the screen parameters.
screen = Screen()
screen.setup(width=X_SIZE, height=Y_SIZE)
screen.bgcolor("black")
screen.title("Game 5, The Snake")
# Disabling the screen tracer so that the animation is displayed once a frame is fully calculated.
screen.tracer(0)

viper = snake.Snake(color="white",initial_direction=0)
serpent = snake.Snake(color="blue", initial_direction=180)

screen.onkey(key="w", fun=serpent.turn_up)
screen.onkey(key="d", fun=serpent.turn_right)
screen.onkey(key="a", fun=serpent.turn_left)
screen.onkey(key="s", fun=serpent.turn_down)

screen.onkey(key="Up", fun=viper.turn_up)
screen.onkey(key="Right", fun=viper.turn_right)
screen.onkey(key="Left", fun=viper.turn_left)
screen.onkey(key="Down", fun=viper.turn_down)


screen.listen()

game_continues = True
dinner = food.Food()
viper_score = scoreboard.Scoreboard(alignment="right")
serpent_score = scoreboard.Scoreboard(alignment="left")

while game_continues:
    if not dinner.isvisible():
        while viper.head.distance(dinner) < 15 or serpent.head.distance(dinner) < 15:
            dinner.change_location()
        dinner.showturtle()
    if viper.alive:
        viper.move_forward()
    if serpent.alive:
        serpent.move_forward()
    if viper.head.distance(dinner) < 15:
        dinner.hideturtle()
        viper.grow_segment()
        viper_score.score += 1
        viper_score.clear()
        viper_score.display_score(viper_score.score, viper.steps)
    if serpent.head.distance(dinner) < 15:
        dinner.hideturtle()
        serpent.grow_segment()
        serpent_score.score += 1
        serpent_score.clear()
        serpent_score.display_score(serpent_score.score, serpent.steps)
    if dinner.position() not in viper.snake_position or dinner.position() not in serpent.snake_position:
        dinner.move()
    screen.update()
    time.sleep(0.2 * abs(1 - max(len(viper.snake), len(serpent.snake))/360) + 0.025)
    # This allows speed to grow up to the point when the snake reaches 360 segments which is 20% of the field.
    # If the player manages to overcome this, they will be rewarded with an increasing speed since then.
    # if viper.head.distance(serpent.head) < 15:
    #     game_continues = False
    for segment in viper.snake:
        if serpent.head.distance(segment) < 15 and serpent.steps > 3:
            game_continues = False
    for segment in serpent.snake:
        if viper.head.distance(segment) < 15 and viper.steps > 3:
            game_continues = False
    viper.check_wall_collision()
    serpent.check_wall_collision()
    viper.check_self_collision()
    serpent.check_self_collision()

    if not viper.alive and not serpent.alive:
        game_continues = False

viper_score.display_final_score(score=viper_score.score, steps=viper.steps)
serpent_score.display_final_score(score=serpent_score.score, steps=serpent.steps)

screen.exitonclick()
