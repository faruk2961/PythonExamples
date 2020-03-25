####Creating Classes####

'''class Point:
    def draw(self):
        print('draw')


point = Point()
print(type(Point))
print(isinstance(point,Point))'''
####Consructors#####

'''class Point:
    #constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x,self.y})')

point = Point(1,2)
point.draw()'''

#####Class vs Instance Attributes####
'''class Point:
    default_color = 'red'  #when we determine an object with class name it effects everything in the class
    #constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x,self.y})')

Point.default_color = 'yellow'
point = Point(1,2)
print(point.default_color)
point.draw()'''
#####Class vs Instance Methods####
'''class Point:
    #constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f'Point ({self.x,self.y})')

point = Point.zero() 
point.draw()'''
######Magic Methods####
'''class Point:
    #constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def draw(self):
        print(f'Point ({self.x,self.y})')

point = Point(1,2)
print(point)'''

######Comparing Objects#####
'''class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point > other)'''
#####Performing Arithmetic Operations#####
'''class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x,self.y + other.y)

point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x)'''
######Making Custom Containers#####
'''class TagCloud:

    def __init__(self):
        self.tags = {} #we initilaze tags attributes to an empty dictionary

    #Here we check if we have this tag in our dictionary,if we don't have it we're going to
    #set it's value to 1. otherwise we're gonna increment it by 1
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1 #0 means if we don't have it we wanna return 0 by default

    #with this implementation we can easily get the number of a given tag
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    #With this implementation we can set the number of  given tag
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    #we can check the lengt og the method
    def __len__(self):
        return len(self.tags)

    #with this function returns an iterator object which gives us one item at a time in for loop
    def __iter__(self):
        return iter(self.tags)
cloud = TagCloud()
cloud['python'] = 10
len(cloud)
cloud.add('Python')
cloud.add('python')
cloud.add('python')
print(cloud.tags)'''
######Properties####
'''class Product:
    def __init__(self,price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value

product = Product(50)
print(product.price)'''
######Inheritance####
'''class Animal:
    def eat(self):
        print('eat')

#Animal:Parent, Base
#Mammal:Child, Sub
class Mammal(Animal):
    def __init__(self):
        self.age = 1

    def walk(self):
        print('walk')


class Fish(Animal):

    def swim(self):
        print('swim')

m = Mammal()
m.eat()
print(m.age)'''
###### The Object Class#####
'''class Animal:
    def eat(self):
        print('eat')

#Animal:Parent, Base
#Mammal:Child, Sub
class Mammal(Animal):
    def __init__(self):
        self.age = 1

    def walk(self):
        print('walk')


class Fish(Animal):

    def swim(self):
        print('swim')

m = Mammal()
print(isinstance(m, Mammal))
print(issubclass(Mammal, Animal))'''
####Method Overriding######
'''class Animal:
    def __init__(self):
        print("Animal Constructure")
        self.age = 1

    def eat(self):
        print('eat')

class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print('walk')

m = Mammal()
print(m.age)
print(m.weight)'''
######Multiple Inheritance#####
'''class Flyer:
    pass

class Swimmer:
    pass

class FlyingFish(Flyer,Swimmer):
    pass

f = FlyingFish()'''
#####A Good Example of Inheritance####
class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def closed(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

#####Abstract Base Classes#####
'''from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def closed(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


stream = FileStream()
print(stream.read)'''
########Polymorphism######
'''from abc import ABC, abstractmethod

class UIControl(ABC):
    pass

class TextBox(UIControl):
    def draw(self):
        print("Text Box")

class DropDownList(UIControl):
    def draw(self):
        print("Drop Down Method")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl,textbox])'''
######Extending Built-in Types######
'''class Text(str):
    def dublicate(self):
        return self + self

text = Text("Python")
print(text.lower())
print(text.dublicate())
class TrackableList(list):
    def append(self, object):
        print('Append called')
        super().append(object)



list = TrackableList()
list.append('1')'''
########Data Classes######
'''from collections import namedtuple

Point = namedtuple('Point',['x', 'y'])



p1 = Point(x=1, y=2)
p1 = Point(x=10, y =2) #if you want to change x you have to define new point variable
p2 = Point(x=1, y=2)
print(p1 == p2)'''


