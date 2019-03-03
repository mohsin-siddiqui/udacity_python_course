import turtle


def base():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_kite()

    window.exitonclick()


def draw_kite():
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(2)
    for i in range(9):
        brad.right(10)
        brad.forward(100)
        for i in range(1, 4):
            brad.right(90)
            brad.forward(100)
    brad.right(75)
    brad.forward(250)


base()
