import turtle

for x in range(8):
    turtle.circle(100)
    turtle.right(45)

for x in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.circle(200)
turtle.done()
