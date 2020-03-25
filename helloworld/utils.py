def find_max(numbers):    #this is a function
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
