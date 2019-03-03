import turtle


def base():
    window = turtle.Screen()
    window.bgcolor("#78B5BA")
    draw_square()
    window.exitonclick()


def draw_square():
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(10)

    brad.begin_fill()
    count = 0
    while count < 36:
        repeat = 0
        while repeat < 4:
            brad.forward(100)
            brad.left(90)
            repeat += 1
        brad.left(10)
        count += 1
    brad.end_fill()


base()
