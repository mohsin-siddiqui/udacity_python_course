import turtle

window = turtle.Screen()
window.bgcolor("white")


pen = turtle.Turtle()
pen.speed(1)
pen.shape("turtle")
pen.color("black")
pen.goto(-100, -75)
pen.right(90)

count = 0
while count < 4:
    pen.forward(200)
    pen.right(90)
    count += 1
pen.left(90)
pen.forward(300)
while count < 6:
    pen.left(90)
    pen.forward(200)
    count += 1

# pen.left(165)
# pen.forward(300)
window.exitonclick()
