import turtle
colors=["red","blue","green","orange","brown","purple"]
turtle.speed(0)
for i in range(900):
    turtle.pencolor(colors[i%2])
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(50)
    turtle.home()
    turtle.right(i)
