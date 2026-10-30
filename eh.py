# BaseException
# Exception
# TypeError, AttributeError, ...

try:
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1/n2)
    # print("hello")
except (ZeroDivisionError,TypeError) as error:
    print("Division Error msg:", error)
except ValueError:
    print("Only provide number in input")
except Exception as error:
    print("Something went wrong:", error)
finally:
    print("Task completed")