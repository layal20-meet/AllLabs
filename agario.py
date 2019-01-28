import turtle
import time
import random
import math
from ball import Ball

running=True
turtle.bgcolor('brown')
BG=turtle.Screen()
BG.bgcolor()
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
running=True
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2

my_ball=Ball(50,100,50,50,70,'blue')
number_of_balls=5
minimum_ball_radius=10
maximum_ball_radius=100
minimum_ball_dx=-5
maximum_ball_dx=5
minimum_ball_dy=-5
maximum_ball_dy=5

BALLS=[]

for i in range(number_of_balls):
    x=random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
    y=random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
    dx=random.randint(minimum_ball_dx , maximum_ball_dx)
    dy=random.randint(minimum_ball_dy , maximum_ball_dy)
    r=random.randint(minimum_ball_radius , maximum_ball_radius)
    color=(random.random(), random.random(), random.random())
    Ball1=Ball(x,y,dx,dy,r,color)
    BALLS.append(Ball1)
    
def move_all_balls():
    for all_balls in BALLS:
        all_balls.move(screen_width, screen_height)

def collide (ball_a,ball_b):
    if ball_a == ball_b:
       return False
    d=math.sqrt((ball_b.xcor()-ball_a.xcor())**2+(ball_b.ycor()-ball_a.ycor())**2)
    if ball_a.r+ ball_b.r >= d:
         return True
    else:
         return False

def check_all_balls_collision():
    global running
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)
    for ball_a in all_balls:
        for ball_b in all_balls:
            if collide(ball_a,ball_b):
                ra=ball_a.r
                rb=ball_b.r
                x=random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
                y=random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
                dx=random.randint(minimum_ball_dx , maximum_ball_dx)
                dy=random.randint(minimum_ball_dy , maximum_ball_dy)
                r=random.randint(minimum_ball_radius , maximum_ball_radius)
                color=(random.random(), random.random(), random.random())
                if ra > rb:
                    small_ball = ball_b
                    big_ball = ball_a
                if ra <= rb:
                    small_ball = ball_a
                    big_ball = ball_b
                if my_ball == small_ball:
                    turtle.write("GAME_OVER",move=False,align='center',font=('Arial',60,'normal'))
                    running=False
                small_ball.new_ball(x,y,dx,dy,r,color)
                big_ball.r+=1
                big_ball.shapesize(big_ball.r/10)
def movearound():
    my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width,screen_height - turtle.getcanvas().winfo_pointery())
while running==True:
    screen_width==turtle.getcanvas().winfo_width()/2
    screen_height==turtle.getcanvas().winfo_height()/2
    movearound()
    move_all_balls()
    check_all_balls_collision()
    turtle.update()
    time.sleep(.1)
turtle.mainloop()
