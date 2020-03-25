####Adding Two Numbers
'''num1 = input("Enter first number:")
num2 = input("Enter second number:")

sum =float(num1) + float(num2)

print(f'The sum of {num1} and {num2} equals {sum}')'''

#####Find the Square Root#####

'''import cmath

num = eval(input("Enter a number: "))

num_sqrt = cmath.sqrt(num)

print(f'Square of {num} is {num_sqrt}')'''
#########Calculate the Area of a Triangle#####
'''a = float(input("Please enter first side: "))
b = float(input("Please enter second side: "))
c = float(input("Please enter third side: "))

# calculate the semi-perimeter
s = (a+b+c)/2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f'The are of triangle is {area}')'''
###########Solve Quadratic Equation####
'''import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(f"The solitions are {sol1} and {sol2}")'''
########Swap Two Variables######

'''x = int(input("Enter x: "))
y = int(input("Enyer y: "))

x, y = y, x

print("x = ", x)
print("y = ", y)'''
##########Generate a Random Number#####
# Program to generate a random number between 0 and 9

# importing the random module
'''import random

print(random.randint(0,9))'''
#########Convert Kilometers to Miles#####

'''km = float(input("Please enter km: "))
miles = km * 0.621371192

print(f'{km} km is equal to {miles} mi')'''

