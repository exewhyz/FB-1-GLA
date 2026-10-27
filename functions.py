
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
    return a+b
    
# print(add_nums(2,6))
# print(f"{add_nums(2,6):.2f}")

# round(number, no_of_decimal_place)
print(round(8.7729,2))