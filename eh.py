# BaseException
# Exception
# TypeError, AttributeError, ...

# try:
#     n1 = int(input("enter first number: "))
#     n2 = int(input("enter second number: "))
#     result = n1 / n2
#     # print("hello")
# except (ZeroDivisionError,TypeError) as error:
#     print("Division Error msg:", error)
# except ValueError:
#     print("Only provide number in input")
# except Exception as error:
#     print("Something went wrong:", error)
# else:
#     print(result)
# finally:
#     print("Task completed")

# raise -> creates exception/error manually in code

# raise ValueError("manually created error")
# raise Exception("manual error")

class NegativeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    # if age < 0 :
    #     raise NegativeError("Age can not be negative.")
    assert age >= 0, "Age can not be negative"
except NegativeError as e:
    print("Error:", e)
except Exception as e:
    print("Other Error:",e)
    
