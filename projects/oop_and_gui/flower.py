import turtle
x = 30
a = 150
b = 30
c = 100

window = turtle.Screen()
window.bgcolor("#99DA00")

artist = turtle.Turtle()
artist.color("blue", "#F9301E")
artist.speed(5)
artist.shape("turtle")

#######################################################################################
artist.begin_fill()
for i in range(1, 37):
    artist.forward(100)
    artist.right(x)
    artist.forward(100)
    artist.right(a)
    artist.forward(100)
    artist.right(b)
    artist.forward(100)
    artist.right(c)

artist.end_fill()
artist.right(90)
artist.forward(250)

window.exitonclick()
