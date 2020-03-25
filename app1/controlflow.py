####Condiotanal Statements####
'''temperature = 10

if temperature > 30:
    print("It's warm")
    print("You can drink water")
elif temperature > 25:
    print("it's nice")
else:
    print("Go Home")
print("Done")'''
######Ternary Operator####
'''age = 10
message = 'Eligible' if age >= 18 else 'Not Eligable'

print(message)'''
####Logical Operators#####
# and
# or
# not
'''high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")'''
######For Loops####
'''for number in range(1,10,2):
    print("Attempts", number + 1, (number +1) * '.')'''
#####For Else####
'''succesful = False
for number in range(3):
    print("Attempts")
    if succesful:
        print("Succesful")
        break
else:
    print("Attemted 3 and Failed")'''
###Nested Loops
'''for x in range(5):
    for y in range(3):
        print(f"({x},{y})")'''
####Iterables#####
'''for x in 'Python':
    print(x)'''
#####While Loop####
'''number = 100
while number > 0:
    print(number)
    number = number // 2'''
'''command = ''
while command.lower() != 'quit':
    command = input(">")
    print("ECHO",command)'''
#####Infinitive loops####
'''command = ''
while True:
    command = input(">")
    print("ECHO",command)
    if command.lower() == 'quit':
        break'''
#####Exercise######
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")



