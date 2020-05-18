# Import modules
import logging

logging.basicConfig(level=logging.DEBUG)


def Dodawanie(a, b):
    return a + b


def Odejmowanie(a, b):
    return a - b


def Mnożenie(a, b):
    return a * b


def Dzielenie(a, b):
    if b == 0:
        return "Don't divide by 0"
    return a / b


calculations = {
    "1": Dodawanie,
    "2": Odejmowanie,
    "3": Mnożenie,
    "4": Dzielenie
}


def get_argument(arg_test):
    while True:
        try:
            arg_test = float(input(arg_test))
        except ValueError:
            print("Enter corret int value")
            continue
        else:
            logging.info(f"Arg_test value is: {arg_test}")
            return arg_test


# Function definitions
def calculator(operation, arg_number_1, arg_number_2, calculations):
    result = round(calculations[operation](arg_number_1, arg_number_2), 2)
    function_name = calculations[operation].__name__

    logging.info(f" {function_name} {arg_number_1} i {arg_number_2}  \n  Wynik to:  {result}")
    return result


# przeniosłem do funkcji poniższy fragment, funkcja bez argumentów)
def calc():
    print('Provide calculation choosing from below list: ')
    for item, calc_type in calculations.items():
        print(item, calc_type.__name__)

    operation = input("Enter correct operator:")
    arg_number_1 = get_argument("Podaj składnik 1. ")
    arg_number_2 = get_argument("Podaj składnik 2. ")

    calculator(operation, arg_number_1, arg_number_2, calculations)


if __name__ == "__main__":
    calc()