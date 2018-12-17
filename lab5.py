from turtle import *
import random
class Square(Turtle):
    def __init__(self,side,color):
        Turtle.__init__(self)
        self.side=side
        self.color=color
        self.shape('square')
        self.shapesize(side*side)
        colormode(255)
    def random_color(self):
        r=random.randint(0,256)
        g=random.randint(0,256)
        b=random.randint(0,256)
        self.color(r,g,b)
s=Square(10,'red')
s.random_color()
s.fd(100)
turtle.mainloop()
