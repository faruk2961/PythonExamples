####Lists#####
'''letters = ["a","b","c"]
matrix = [[0,1],[2,4]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(numbers)
print(len(chars))'''
###Accessing Items####
'''letters = ['a','b','c','d']
letters[0] = 'A'
print(letters)'''
'''numbers = list(range(20))
print(numbers[::2]) #this will return all the even numbers in the list
print(numbers[::-1]) #this will return the list in reverse order'''
####Unpacking Lists#####
'''numbers = [1, 2, 3]
first, second, third = numbers #this called list unpacking'''

'''numbers = [1, 2, 3,4,4,4,4,]
first, second, *others = numbers
print(first, second)'''
####Looping over Lists#####
letters = ['a','b','c']
'''for letter in letters:
    print(letter)'''
'''for letter in enumerate(letters): #enumerate will give us a tupple of two items
    print(letter)'''
'''for index, letter in enumerate(letters): #we can uniterate the tupple
    print(index,letter)'''
####Adding and Removing Items####
'''letters = ['a','b','c']
#Add
letters.append('d')
letters.insert(0,"-")
print(letters)
#Remove
letters.pop() #removes the last item in the list
letters.remove('b') #removes firs 'b' in the list
del letters[0:3] #removes a range of item in the list
letter.clear() #clear the list 
print(letters)'''
#####Finding Items#####
'''letters = ['a','b','c']
print(letters.index('a'))''' #this will return the index of the given item
####Sorting Lists####
'''numbers = [3,51,8,2,6]
numbers.sort()
numbers.sort(reverse=True) #this sorts the list from bigger to smaller
print(sorted(numbers)) #this will create a new list with sorted numbers
print(numbers)'''
'''items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]


def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)'''
#####Lambda Functions####
##if we want to use function only one time we use lambda
##(key = lambda parameters:expression
'''items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]
items.sort(key=lambda item:item[1])
print(items)'''
#####Map Functions#####
'''items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]
prices = list(map(lambda item:item[1],items))
print(prices)'''
####Filter Functions####
'''items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]
filtered = list(filter(lambda item:item[1] >= 10, items))
print(filtered)'''
######List Comprehensions####
'''items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]
prices = [item[1] for item in items] #this can be used for map functions
print(prices)
prices = [item for item in items if item[1] >= 10]
print(prices) #this can be used for filter functions'''
#####Zip Function#####
'''list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1,list2)))'''
####Stacks####
'''browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
if not browsing_session:
    print('disable')
print('redirected',browsing_session[-1])'''
####Queues#####
'''from _collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")'''
#####Tuples####
'''point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print('Exists')
else:
    print('Not exists')'''
####Swapping Variables
'''x = 10
y = 11

x, y = y, x
print("x= ",x,"\ny= ",y)'''
####Arrays####
'''from array import array
numbers = array("i",[1, 2, 3])
print(numbers)'''
#####Sets####
'''numbers = [1,1,3,5,6,6]
first = set(numbers)
second = {1,7}
print(first | second) #this returns first list and second list with unique numbers
print(first & second) #this returns the same item that both list have
print(first - second) #this returns different item between lists
print(first ^ second) #this returns semantic difference'''
####Dictionaries#####
'''point = dict(x = 1,y = 2)
point['x'] = 10
point['z'] =20
if 'a' in point:
    print(point['a'])
print(point.get('a', 0))
del point['x']
print(point)
for key, value in point.items():
    print(key, value)'''
####Dictionary Comprehensions####

#comprehension = [expression for item in items]

'''values = {x:x * 2 for x in range(5)}
print(values)'''
#####Generator Expressions####
#when we deal with big range of data we should use parantezis "() " to avoid extra memory use
'''from sys import getsizeof

values = (x * 2 for x in range(10000))
print("gen:",getsizeof(values))
values = [x * 2 for x in range(10000)]
print("list:",getsizeof(values))'''
#######Unpacking Operator####
'''numbers = [1, 2, 3]
print(*numbers)'''

'''values =list(range(5))
values = [*range(5),*'Hello']
print(values)'''

'''first = [1, 2]
second = [3]
values = [*first , *second]
print(values)'''

'''first = {"x": 1}
second = {"x": 10,"y":20}
combined = {**first,**second, "z":4}
print(combined)'''
#####Exercise####
'''sentence = "This is a common interview question"
char_frequence = {}

for char in sentence:
    if char in char_frequence:
        char_frequence[char] += 1
    else:
        char_frequence[char] = 1

char_frequence_sorted = sorted(char_frequence.items(),
                               key=lambda kv:kv[1],
                               reverse=True)
print(char_frequence_sorted[0])'''





