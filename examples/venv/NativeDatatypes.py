#### Program to add two matrices using nested loop####

'''X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)'''
######Transpose a Matrix#####
'''X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]
for r in result:
    print(r)'''
######Multiply Two Matrices#####
# 3x3 matrix
'''X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] +=X[i][k] * Y[k][j]
for r in result:
    print(r)'''
#########Check Whether a String is Palindrome or Not####
'''my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is a palindrome")
else:
    print("The string is not polindrome")'''
#####Remove Punctuations From a String####

'''# define punctuation
punctuations = !()-[]{};:'"\,<>./?@#$%^&*_~

my_str = "Hello!!!, he said ---and went."

# remove punctuation from the string
no_punc = ''
for char in my_str:
    if char not in punctuations:
        no_punc = no_punc + char

# display the unpunctuated string
print(no_punc)'''
#####Sort Words in Alphabetic Order####
'''my_str = "Hello this Is an Example With cased letters"

# breakdown the string into a list of words
words = my_str.split()

#sort the list
words.sort()

#display the sordet words
print("The sordet words are: ")
for word in words:
    print(word)'''
######Illustrate Different Set Operations#####

''''# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)'''
#####Count the Number of Each Vowel#####
# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()


# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1

print(count)

