'''numbers = (1, 2, 3)# this is a tuple that we can not modify
print(numbers[0])'''
#####UNPACKING####
'''coordinates = (1 ,2 ,3)
x, y, z = coordinates # this is unpacking
print(x)'''
#####DICTIONARIES#######
#We use dictionaries in stuations where we want to store information that comes as key value pairs.
'''customer = {
    "name" : "Faruk",
    "age":26,
    "is_verified": True
}    #With these curly braces we can define dictionary
customer["birthday"] = "29.03.1994" #we can add new key value into dictionary like this
print(customer["birthday"])'''
#######EXAMPLE########
'''phone = input("Phone: ")
digits_mapping = {
    "1" : "one",
    "2" :"two",
    "3" :"three",
    "4" :"four"
    }
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)'''
#######EMOJI CONVERTER####
'''mesage = input(">")
words = mesage.split(' ')
emojies = {
    ":)" : "😃",
    ":(" :"😞"
}
output = ''
for word in words:
    output += emojies.get(word,word) + " "
print(output)'''
######FUNCTIONS#######





