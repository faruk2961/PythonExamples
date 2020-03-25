'''print("Faruk Furkan KOC")
print('o----')
print('  ||||')
print("*" * 10)'''
########variables#######
'''price = 10 #integer
rating = 4.9 #float
name = 'faruk' #string
is_published = True #boolean
print(price)'''
########EXAMPLE######
'''full_name = "John Smith"
age = 20
is_new = True'''
#######GETTING INPUT########
'''name = input("Whats is your name ? ")
print("Hi " + name)'''
#######EXAMPLE######
'''p_name = input ("What is your name? ")
f_color = input ("What is your favorite color? ")
print(p_name + " likes " + f_color)'''
########TYPE CONVERSION########
'''birth_year = input("Please enter your birtyear: ") #when you get input function you always get string 
age = 2020 -  int(birth_year)
print(type(age)) # type funtion shows us what is the type of  the  value
print(age)'''
#######EXAMPLE#######
'''weight = input('Please enter your weight in pouns:')
kg = 0.45 * int(weight)
print(kg)'''
#######STRINGS######
'''course = 'Pyhton course for Beginners'

print(course[0:3])'''
######FORMATED STRINGS######
'''first = 'John'
last = 'Smith'
message= first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder' #we call this formated string f'
print(msg)'''
######STRING METHODS#####
'''course = 'Pyhton course for Beginners'
print(len(course))
print(course.upper()) ##upper helps us to display the characters in Uppercase
print(course.lower()) ##lower helps us to display the characters in Lowercase
print(course.find('o')) #this will return the index of the first occurence
print(course.replace("Beginners","Absolut Beginners")) #replace helps us replace what we want with other
print('Pyhton' in course) # we are checking to see if phyton is in the course variable'''
#######ARITMETIC OPERATIONS#########
'''x = 10
x -=3
print(x)'''
#######OPERATOR PRECEDENCE#######
'''x = (10 + 3) * 2 ** 3 # answer is 104 because it calculates parantesis first
print(x)'''
######MATH FUNCTIONS#######
'''import math
x = 2.9
print(round(x)) #answer will be 3
print(abs(-2.9)) #answer will be 2.9 abs mean absolute it always returns positive numbers
print(math.ceil(2.9)) #answer will be 3
print(math.floor(2.9)) # answer will be 2'''



