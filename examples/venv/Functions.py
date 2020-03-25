#####Display Powers of 2 Using Anonymous Function#####

'''terms = int(input('How many terms ?'))

# use anonymous function

result = list(map(lambda x: 2 ** x, range(terms)))

print("Total terms are", terms)

for i in range(terms):
    print("2 raised to power", i,"is", result[i])'''
#########Find Numbers Divisible by Another Number######

''''# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x:(x % 17 == 0), my_list))

print("Numbers divisible by 17 are:", result)'''
########Convert Decimal to Binary, Octal and Hexadecimal####
'''dec = 500

print('The decimal value of',dec,"is")

print(bin(dec),"in binary.")
print(oct(dec),"in octal")
print(hex(dec),"in hexadecimal")'''
#######Find ASCII Value of Character#####
'''c = 'r'

print("The ASCII of'" + c +"'is",ord(c))'''

#####Find HCF or GCD####
'''def compute_hcf(x , y):
    while(y):
        x , y = y , (x % y)

    return x
hcf = compute_hcf(300, 400)
print("The HCF is ",hcf)'''
#####Find LCM####
'''# This function computes GCD

def compute_gcd(x , y):
    while (y):
        x, y = y, (x % y)
    return x

# This function computes LCM

def compute_lcm(x, y):
    lcm = (x * y)// compute_gcd(x,y)
    return lcm

num1 = 54
num2 = 24

print("L.C.M is",compute_lcm(num1,num2))'''
#########Find the Factors of a Number########
'''def print_factors(x):
    print("The factors of",x,"are :")

    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 345
print_factors(num)'''
#######Make a Simple Calculator#####
'''def add(x , y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y

print("Select operation")
print("1. Add")
print("2. Substrack")
print("3. Multiply")
print("4, Divide")

choice = input("Enter (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice =="1":
    print(num1, "+", num2, "=",add(num1,num2))
elif choice =="2":
    print(num1, "-", num2, "=",substract(num1,num2))
elif choice =="3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid number")'''
######Shuffle Deck of Cards#####
# importing modules
'''import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),["Spade","Heart","Diamond","Club"]))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got: ")
for i in range(4):
    print(deck[i][0],"of",deck[i][1])'''
########Display Calendar#######
'''import calendar

yy = int(input("Please enter year: "))
mm = int(input("Please enter month: "))
# display the calendar
print(calendar.month(yy, mm))'''
#######Display Fibonacci Sequence Using Recursion######
'''def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

nterms = 20
if nterms <= 0:
    print("Please enter positive integer ")
else:
    print("Fibonacci Sequences Are:")
    for i in range(nterms):
        print(recur_fibo(i))'''
########Find Sum of Natural Numbers Using Recursion#####
'''def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

num = 34

if num <= 0:
    print("Please enter positive number")
else:
    print("The sum is",recur_sum(num))'''
##########Find Factorial of Number Using Recursion#####
'''def recor_factorial(n):
    if n == 1:
        return n
    else:
        return n * recor_factorial(n-1)

num = 5

if num < 0:
    print("Sorry, Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num,"is",recor_factorial(num))'''
#########Convert Decimal to Binary Using Recursion######
def converToBinary(n):
    if n > 1:
        converToBinary(n // 2)
    print(n % 2,end = "")

dec = 30
converToBinary(dec)
print()











