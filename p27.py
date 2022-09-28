#10 Write a python script to implemented a nested Try Except block
print("Start")
try:
    a=int('a')
    b=int(input("Enter number: "))
except ValueError:
    print("Value Error")
    try:
        a=int('23')
    except ValueError:
        print("Value Error")
print("End")

#9 Write a python script to raise a ValueError.
#8 Write a python script to implement try except and else block for division
#7 Write a python script to add a finally block for the above script
#6 Write a python script to create a calculator with 4 basic operations,
#  and handle a maximum number of exceptions.
from decimal import InvalidOperation
from logging import exception
try:
    n1=int(input("Enter first number: "))
    op=input("Enter operation(+,-,*,/): ")
    n2=int(input("Enter second number: "))
    res=n1+n2 if op=='+' else n1-n2 if op=='-' else n1*n2 if op=='*' else n1/n2 if op=='/' else 'Invalid'
    if res=='Invalid':
        raise InvalidOperation
except ZeroDivisionError:
    print("Zero division error")
except FloatingPointError:
    print("Floating point error")
except OverflowError:
    print("Over flow error")
except ValueError:
    print("Value error")
except InvalidOperation:
    print("Invalid Operator")
except Exception:
    print("Exception")
else:
    print(n1,op,n2,"=",res)
finally:
    print("Operation ended")

#5 Write a python script to handle multiple Exception in one try
from ast import ExceptHandler
print("Start")
try:
    c=100/0
    a=int('a')
    b=int(input("Enter number: "))
except ValueError:
    print("Value Error")
except ArithmeticError:
    print("Arithmetic Error")
except Exception:
    print("Exception")
finally:
    print("finally")
print("End")

#4 Write a python script to handle a ValueError
print("Start")
try:
    a=int('a')
    b=int(input("Enter number: "))
except ValueError:
    print("Value Error")
print("End")

#3 Write a python script to handle the ArithmeticError
print("Start")
try:
    a=100/0
except ArithmeticError:
    print("Arithmetic Error")
print("End")

#2 Write a python script to create a ValueError
print("Start")
a=int('a')
b=int(input("Enter number: "))
print("End")

#1 Write a python script to create a ArithmeticError
print("Start")
a=100/0
print("End")