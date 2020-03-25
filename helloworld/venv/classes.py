'''class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.draw()
print(point1.x)

point2 = Point()
point2.x = 50
print(point2.x)'''

######CONSTRUCTORS######
'''class Point:
    def __init__(self, x, y):   #init short for initialized, this method use construck an object
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point(10, 20)
print(point1.x)'''
'''class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name}")


faruk = Person("Faruk")
faruk.talk()
bob = Person("Bob Smith")
bob.talk()'''
#######INHERITANCE#######
'''class Mammal:
class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def annoying(self):
        print("Annoying")
cat1 = Cat()
cat1.annoying()'''

