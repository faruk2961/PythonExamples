######LISTS######
'''names = ["Faruk", "Alihan", "Emre","Murat"]
names[0] = 'Far' # it update the faruk as far because faruk is in 0 index
print(names[2:4])
print(names)'''
######EXAMPLE######
#find the largest number
'''numbers = [1,2,3,4,5,6]
max  = numbers[0]
for number in numbers:
    if number > max:
        max  = number
print(max)'''
#######2D LISTS######
'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix [0] [1])
for row in matrix:
    for item in row:
        print(item)'''
#######LIST METHODS######
'''numbers = [5, 2, 7, 5, 4]
numbers.append(20)# append adds new number to the list
numbers.insert(1 , 29) #insert used for add number whicever index we want fist number is the index second number which we wanna add
numbers.remove(7) #remove used for remove a number from the list
numbers.clear() # if you wanna remove all the numbers in the list use clear
numbers.pop() # pop used for remove the last number in the list
numbers.index(5) #if we want to check for the existence of an item in our list, we can call the index method
print(50 in numbers) # we are checking for the existence of 50 in the list of numbers
print(numbers.count(5)) #it shows how many 5 we have in the list
numbers.sort() # it sorts the list
numbers.reverse()#this simply reverses our list
numbers2 = numbers.copy() # numbers2 is copy of numbers, if you do any change in original list it's not gonna impact numbers2
print(numbers)'''
#######EXAMPLE#########
'''numbers = [3, 5, 6, 19, 3, 5, 20]
unique = []
for x in numbers:
    if x not in unique:
        unique.append(x)
print(unique)'''

