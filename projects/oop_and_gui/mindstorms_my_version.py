import turtle


def base():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()


def draw_square():
    brad = turtle.Turtle()
    brad.color("Green")
    brad.shape("turtle")
    brad.speed(1)

    repeat = 0
    while repeat < 4:
        brad.forward(100)
        brad.right(90)
        repeat += 1


def draw_circle():
    mohsin = turtle.Turtle()
    mohsin.color("Yellow")
    mohsin.shape("arrow")
    mohsin.speed(1)

    mohsin.circle(100)


def draw_triangle():
    david = turtle.Turtle()
    david.color("black")
    david.shape("turtle")
    david.speed(1)

    david.right(150)
    david.forward(200)
    david.left(150)
    david.forward(165)


base()
