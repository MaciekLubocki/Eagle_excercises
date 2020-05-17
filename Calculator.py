# Import modules
import logging

logging.basicConfig(level=logging.DEBUG)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Don't divide by 0"
    return a / b


calculations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def get_argument(arg_test):
    while True:
        try:
            arg_test = int(input(arg_test))
        except ValueError:
            print("Enter corret int value")
            continue
        else:
            logging.info(f"Arg_test value is: {arg_test}")
            return arg_test


# Function definitions
def calculator(operation, arg_number_1, arg_number_2, calculations):
    # zmiana z print na loggin plus złamanie linii
    result = calculations[operation](arg_number_1, arg_number_2)
    function_name = calculations[operation].__name__

    logging.info(f"You have chosen {function_name}. So: {arg_number_1} {operation} {arg_number_2} = {result}")
    return result


# przeniosłem do funkcji poniższy fragment, funkcja bez argumentów)
def calc():
    print('What do you want me to do (choose appropriate number): ')
    for item in calculations:
        print(item)

    operation = input("Enter correct operator:")
    arg_number_1 = get_argument("Enter first number: ")
    arg_number_2 = get_argument("Enter second number: ")

    calculator(operation, arg_number_1, arg_number_2, calculations)


if __name__ == "__main__":
    calc()