# Stings are immutable

"""
CRUD Operations

CREATE => Not Possible => AtrributeError (append,insert,extend)
READ => Possible
UPDATE => Not Possible => TypeError
DELETE => Not Possible => AtrributeError(pop,remove,clear) or TypeError (del keyword)
"""


"""
# Hello
Negative_INDEX    Postive_INDEX     CHAR
-5                0                 H
-4                1                 e
-3                2                 l
-2                3                 l
-1                4                 o                 
"""

text = "Python Programming"
# print(text[::-1])
# print(len(text))
# print(type(text))
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])

# Empty String
t = "" or '' or """""" or ''''''

# print(len(t))
# print(bool(t))
# print(bool(len(t)))


# take input and check that string is palindrome or not

# word = input("Enter your word: ")
# if word == word[::-1]:
#     print("It is Palindrome")
# else:    
#     print("It is not Palindrome")


# string concatination and replication

print("hello"+ " " * 5 + "world") # "hello" + "     " + "world"
print("hello " * 5)

# "hello" + "hello" + "hello" + "hello" + "hello"
# "hellohellohellohellohello"