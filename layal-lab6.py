from turtle import*
import math
import random
class ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius=radius
        self.color(color)
        self.speed(speed)
ball1 = ball(150,'red',10)
ball2 = ball(100,'blue',10)

def check_collision(ball1,ball2):
    if ball1.radius + ball2.radius > math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)):
        print('collision')
    else:
        print('no collision')
        
