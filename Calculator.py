
# Import modules

import logging

logging.basicConfig(level=logging.DEBUG)


# tutaj przeniosłem deklarację function_name mam błąd związany ze zmiennymi calculations/operation...co z tym zrobić?
function_name = calculations[operation].__name__

# Function definitions
def calculator(arg_number_1, arg_number_2):
    
# zmiana z print na loggin plus złamanie linii
    logging.info("You have chosen ", function_name, ". So: ", arg_number_1, operation  ,arg_number_2, "=", 
    calculations[operation](arg_number_1, arg_number_2))
   
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


def get_argument(arg_test):
    while True:
        try:
            arg_test = int(input(arg_test))
        except ValueError: 
            print ("Enter corret int value")
            continue
        else:   
            logging.info("Arg_test value is: ", arg_test)
            return arg_test
            
            
#przeniosłem do funkcji poniższy fragment, funkcja bez argumentów)
def calc():

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
                
        arg_number_1 = get_argument("Enter first number: ")
        arg_number_2 = get_argument("Enter second number: ")
    
        return arg_number_1, arg_number_2;
    
    logging.info(calc())

#chciałem wywołać funkcję w funkcji ale komunikuje że nie zna drugiej zmiennej którą przecież zawarłem w funkcji calc() i oddaję w return
calculator(calc())


