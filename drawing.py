import turtle

def draw_square(some_turle):
    for i in range(1,5):
        some_turle.forward(100)
        some_turle.right(90)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)

    for i in range(1,36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_shape()
