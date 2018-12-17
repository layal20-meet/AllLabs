class Rectangle(object):
	def_init_(self, width, height):
		self.width = width
		self.height = height
	def Area(self):
		return self.width*self.height
	def Perimeter(self):
		return(self.width + self.height)*2
Rectangle1(20.25)
print(Rectangle1.Area())
print(Rectaangle1.Perimeter())

class Person(object):
    def __init__(self,name,age,city,gender,weight):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender
        self.weight=weight
    def eat_breakfast(self):
        input("what is your favorite breakfast?")
        x=int(input ("how much does this meal weigh?"))
        self.weight+=x
        print(self.weight)
seraj=Person("seraj",15,"iksal","male",56)
seraj.eat_breakfast()
