
# Import modules

import logging
import string
import inspect
import sys

logging.basicConfig(level=logging.DEBUG)

# Function definitions
def calculator(arg_number_1, arg_number_2):
    print("You have chosen ", function_name, ". So: ", arg_number_1, operation  ,arg_number_2, "=", calculations[operation](arg_number_1, arg_number_2))
   
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


def testify(arg_test):
    while True:
        try:
            arg_test = int(input(arg_test))
        except ValueError: 
            print ("Enter corret int value")
            continue
        else:   
            logging.info("Arg_test value is: ", arg_test)
            return arg_test
            break
            


# Executable part of code
if __name__ == "__main__":


    calculations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    print('What do you want me to do (choose appropriate number): ')
    for item in calculations:
        print(item)


    
    operation = input("Enter correct operator:")
    function_name = calculations[operation].__name__
    

arg_number_1 = testify("Enter first number: ")
arg_number_2 = testify("Enter second number: ")


calculator(arg_number_1, arg_number_2)


