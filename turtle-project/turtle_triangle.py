import turtle

def draw_triangle(some_turtle, side_size):
    some_turtle.left(60)
    for i in range(1,4):
        some_turtle.forward(100/side_size)
        some_turtle.right(120)

    some_turtle.right(60)
    some_turtle.forward(100/side_size)

def set_initial_position(turtle):
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-100)
    turtle.pendown()

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    my_turtle = turtle.Turtle()
    my_turtle.color("green")

    set_initial_position(my_turtle)

    for i in range(1,4):
        for i in range(1,5):
            draw_triangle(my_turtle, 1)
        my_turtle.left(120)

    for i in range(1,4):
        for i in range(1,5):
            draw_triangle(my_turtle, 2)
            my_turtle.fill(True)
        my_turtle.left(120)

    my_turtle.forward(200)

    for i in range(1,4):
        for i in range(1,5):
            draw_triangle(my_turtle, 2)
            my_turtle.fill(True)
        my_turtle.left(120)

    my_turtle.left(60)
    my_turtle.forward(200)
    my_turtle.left(60)

    for i in range(1,4):
        for i in range(1,5):
            draw_triangle(my_turtle, 2)
        my_turtle.left(120)

    window.exitonclick()

draw_art()
