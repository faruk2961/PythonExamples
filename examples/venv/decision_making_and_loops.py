##########Check if a Number is Positive, Negative or 0#######

'''num = float(input('Please enter a number: '))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f'{num} is negative')
else:
    print(f'{num} is equal to 0')'''
#######Check if a Number is Odd or Even#####

'''num = float(input("Enter a number: "))

if (num % 2) == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')'''
######Check Leap Year####
'''year = int(input("Please enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a  leap year(it has 366 days)')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')'''
#########Find the Largest Among Three Numbers#####
'''num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
    print(f"{num1} is the biggest number")

elif (num2 >= num3) and (num2 >= num3):
    print(f'{num2} is biggest number ')
else :
    print(f'{num3} is the biggest number')'''
########Check Prime Number#####
'''num = int(input("Enter a number: "))

if num > 1:
    for i in range(2,num):
        if (i % 2) == 0:
            print(f"{num} not a prime number")
            print(i, "times",num//i,"is",num)
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f'{num} is not a prime number')'''
###########Print all Prime Numbers in an Interval#####
'''lower = 900
upper = 1000

print("Prime numbers between",lower, "and",upper)

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if num % 2 == 0:
                break
        else:
            print(num)'''
###########Find the Factorial of a Number######
'''num = int(input('Enter a number: '))
factorial = 1
if num == 0:
    print("The factorial 0 is 0")
elif num < 0:
    print("Sorry, negative numbers of factorial is not exist")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f'The factorial of {num} is {factorial}')'''
#########Display the multiplication Table######
'''num = 10
for num in range(1, 11):
    for i in range(1,11):
        print(num, 'x', i, '=', num*i)'''
##########Print the Fibonacci sequence#######
'''def recur_fibo(n):
    if n <=1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
nterms = int(input("Enter a number "))

if nterms < 0 :
    print('Please enter positive integar')

else:
    print('Fibonacci sequence: ')
    for i in range(nterms):
        print(recur_fibo(i))'''
##########Python Program to Check Armstrong Number#####
'''num  = int(input("Please enter a number: "))

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# display the result
if num == sum :
    print(f"{num} is an armstrong number")
else:
    print(f'{num} is not an armstrong number')'''
##########Find Armstrong Number in an Interval########
'''low = 100
upper = 2000

for num in range(low, upper +1):

    order = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)'''
########Find the Sum of Natural Numbers#####
'''num = 17


if num < 0 :
    print('Please enter positive number')
else:
    sum = 0

    while num > 0:
        sum += num
        num -= 1
    print('The sum is', sum)'''












