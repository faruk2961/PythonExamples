####Defining Functions####
'''def greet():
    print("Hi there")
    print("Welcome aboard")


greet()'''
######Arguments####
'''def greet(first_name, last_name): #we define parameters here
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Faruk", "Koc") #we define arguments here
greet("Emre", "Yilmaz")'''
#####Types of Functions####
# 1- Perform a Task
# 2- Return a Value

'''def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Faruk")
print(message)'''
####Keyword Arguments####
'''def increment(number, by):
    return number + by

print(increment(2, by=1)) #by is keyword argument'''
####Xargs#####
'''def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

message = multiply(2,3,4,5)
print(message)'''
#####XXargs####
'''def save_user(**user):
    print(user["age"])

save_user(id=1, name="Faruk", age=26)'''
####Exercise###
'''def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"

    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input
print(fizz_buzz(15))'''


