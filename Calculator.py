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
            # logging.info(f"Arg_test value is: {arg_test}")
            return arg_test


# Function definitions
def calculator(operation, arg_number_1, arg_number_2, calculations):
    result = round(calculations[operation](arg_number_1, arg_number_2), 2)
    function_name = calculations[operation].__name__
    
    result_text = (f""" {function_name} {arg_number_1} i {arg_number_2} \n""")
    result_text += (f" Wynik to:  {result}")
    print(result_text)

    return result


def calc():
    print('Podaj działanie, posługując się odpowiednią liczbą: ')
    # for item, calc_type in calculations.items():
    #     print(item, calc_type.__name__)

    for item, calc_type in calculations.items():
         print(item, calc_type.__name__, end=" ")
        
    operation = input()
    arg_number_1 = get_argument("Podaj składnik 1. ")
    arg_number_2 = get_argument("Podaj składnik 2. ")

    calculator(operation, arg_number_1, arg_number_2, calculations)


if __name__ == "__main__":
    calc()