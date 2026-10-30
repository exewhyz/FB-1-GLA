
# for i in range(1,10):
#     print(i * 2)
    
# for i in range(1,5):
#     print(i * 2)
    
# for i in range(1,7):
#     print(i * 2)
    
"""
Components of function

1. function definition => create
2. function call => use
"""

# Syntax

# def fn_name():
#     logic

def greet():     # function definition
    print("Hello Aniket")
    
# greet()         # function call
# greet()
# greet()
# greet()
# greet()

# def double_and_print():
#     for i in range(1,10):
#         print(i * 2)
        
# double_and_print()
# double_and_print()


# prameter and argument

# parameter => fn accept => create/define
# argument => actual data => call


"""
Types of parameter/argument
1. Required
2. Default
3. Postional
4. keyword
"""


def double_and_print(a,b):
    for i in range(a, b):
        print(i * 2)

# double_and_print(1, 10)
# double_and_print(1,8)
# double_and_print(1,b=6)

# *args - tuple
# **kwargs - dict

nums = [1,4,5,2,3,9,11]

# def add(*numbers):
#     print(sum(numbers))
    
# add(1,3,8,9,0)

# def details(**kwargs):
#     for key,value in list(kwargs.items()):
#         print(f"{key}: {value}")

# details(name="Aniket", email="aniket@test.com", phone=9876543210)
# print("-"*30)
# details(name="Piyush", email="piyush@test.com")

# def create_event(event_name, *contri, **event_lead_deatils):
#     print("Event Name:", event_name)
#     total_count= len(contri)
#     total_contri = sum(contri)
#     average = total_contri / total_count
#     print("Total Contributors:", total_count)
#     print("Total Contribution:", total_contri)
#     print("Average Contribution:", average)
#     print("Event Leader Details:")
#     for key,value in list(event_lead_deatils.items()):
#         print(f"{key}: {value}")
        
# create_event("Impulse", 5,11,21,2,7, name="Mayank Roy", email="mayank@gla.in", phone = 9876543210 )

# return keyword

def add_nums(a,b):
    print("hii")
    return a+b
    print("hello")
    
# we can retrun multiple values using return keyword but can't use multiple return keyword in a function
# nothing will execute after return line in a function
# function will exit after returning the values
    
# print(add_nums(2,6))
# print(f"{add_nums(2,6):.2f}")

# round(number, no_of_decimal_place)
# print(round(8.7729,2))

# lambda function

def double(x):
    return x * 2

# print(double(5))

db = lambda x : x * 2
# print(db(6))

# print((lambda a,b : a + b)(1,3)) #iifi

# add = lambda a,b : a + b
# print(add(3,8))

# callback - function as argument
# hof - function that accepts function as an argument

# def add(a,b):
#     return a+b
add = lambda a,b : a+b
# def sub(a,b):
#     return a-b
sub = lambda a,b : a-b
# def mul(a,b):
#     return a*b
mul = lambda a,b : a*b

def calculate(x,y,operation):
    result = operation(x,y)
    print(result)

# calculate(4,3, add)
# calculate(4,3, lambda a,b : a+b)

# map, filter, reduce

# nums = [34, 2, 21, 17 ,14, 96]

# for v in nums:
#     print(v)
even = [] 

# n = []
# for i in range(1,10):
#     n.append(i * 2)
# print(n)

# map(callback, iterable) -> map
# iterable - str,list,tuple,set, range()

# def d(a):
#     return a * 2
# print(set(map(d, range(1,10))))

# print(set(map(lambda a:a*2, range(1,10))))

# local scope and global scope

# x = 5

# def check():
#     global x
#     x = 10
#     print("Inside fn",x)

# check()
# print("Outside fn",x)

# filter(callback, iterable) -> filter

products = [{"name":"P1", "color":"red", "price": 1000}, 
    {"name":"P2", "color":"yellow", "price": 2000},
    {"name":"P3", "color":"black", "price": 3000}]

# filtered_data = []
# for p in products:
#     if p["color"] == "black":
#         filtered_data.append(p)
# print(filtered_data)

print(list(filter(lambda x: x["color"] == "black", products)))

# print([x for x in products if x["color"] == "black"])