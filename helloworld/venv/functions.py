#####FUNCTIONS######
'''def greet_user():
    print("Hi there!")
    print("How is it going")


print("Start")
greet_user()
print("Finish")'''
#######PARAMETERS######
'''def greet_user(first_name,last_name):      #name is the parametr
    print(f"Hi {first_name} {last_name}!")
    print("How is it going")


print("Start")
greet_user("faruk","furkan")
print("Finish")'''
######KEYWORD ARGUMENTS######
'''def greet_user(first_name,last_name):      #name is the parametr
    print(f"Hi {first_name} {last_name}!")
    print("How is it going")


print("Start")
greet_user(first_name="faruk",last_name="furkan") #if we define first_name and last_name here they are keyword arguments
print("Finish")'''
#########RETURN STATEMENT#######
'''def square(number):
    return number * number

print(square(3))'''
#####CREATING A REUSABLE FUNCTIONS#####
'''def emoji_converter(message):
    words = message.split(' ')
    emojies = {
        ":)" : "😃",
        ":(" :"😞"
    }
    output = ''
    for word in words:
            output += emojies.get(word,word) + " "
    return output
message = input(">")
print(emoji_converter(message))'''

