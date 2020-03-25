try:
    age = int(input("Age:"))
    income  = 1000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can not be 0.")
except ValueError:
    print("Invalid Value")


