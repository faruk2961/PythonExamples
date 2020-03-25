#######WHILE LOOPS######
"""i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")"""
######GUESSING GAME#####
'''guess_count = 0
guess_limit = 3
secret_number  = 9
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!!")
        break
else:
    print("Sorry, you failed!")'''
########Car Game #########
'''command  = ""
car_started = False
while True:
    command = input(">").lower()
    if command == "start":
        if car_started :
            print("Car already started")
        else:
            car_started = True
            print("Car started")

    elif command == "stop":
        if not car_started:
            print("Car is already stopped")
        else:
            car_started = False
            print("Car stopped")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - quit the program
        """)
    else:
        print("Sorry I don't understand that")'''
########FOR LOOPS########
'''for item in 'Python':  we can loop the python starting p to n
    print(item)
for item in ["Faruk", "Alihan", "Emre"]: #we can loop a list  
    print(item)
for item in range(10): #it creates a range of number 
    print(item)'''
#####EXAMPLE######
'''prices = [10 , 20 , 30 ]
total = 0
for price in prices:
    total += price
    print(f"Total: {total}")'''
#########NESTED LOOPS#######
'''for x in range(4):
    for y in range(3): #inner loop
        print(f"({x},{y})")'''
######EXAMPLE######
'''numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)'''




