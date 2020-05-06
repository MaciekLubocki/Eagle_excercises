# a = 1

# def scope_demo():
#     a = 2
#     print(a)

# scope_demo()
# print(a)


# def shopping():
#     shopping_items = [
#         "jajka",
#         "bułka",
#         "ser feta",
#         "masło",
#         "pomidor"
#     ]
#     shopping_cart = "Koszyk zawiera: "
#     for item in shopping_items:
#         shopping_cart += item + '\n'
#     return shopping_cart

# print(shopping())



# def no_result_function():
#     print("I am just printing I love you")
#     print("and returning nothing to you!")  
#     return None
# print(type(None))



# def day_times():
#     return "morning", "afternoon", "evening", "night"

# times = day_times()
# print(times)
# print(type(times))


# shopping_items = [
#     "jajka",
#     "bułka",
#     "ser feta",
#     "masło",
#     "pomidor"

# ]

# def shopping(items):
#     shopping_cart = "Koszyk zawiera: "
#     for item in items:
#         shopping_cart += item + '\n'
#     return shopping_cart

# basket = shopping(shopping_items)
# print(basket)


# def shopping(items, payment='card', shop='local'):
#     pass
# print(shopping_items, payment, shop);



# shopping_items = [
#     "jajka",
#     "bułka",
#     "ser feta",
#     "masło",
#     "pomidor"
# ]



# def shopping(items, payment='card', shop='local'):
#     pass
# print(shopping(shopping_items, payment='cash'))



# def count_them_all(*args, **kwargs):
#     positional_args_count = len(args)
#     print(f"I have received {positional_args_count} positional arguments")

# count_them_all(1, 2, 3, "A", a=1, b=2)

# def customized_hello(first_name, last_name, gender_prefix='Mr'):
#     """
#         Prints hello, based on arguments passed
#         Arguments:
#         first_name,
#         last_name
#         Optional arguments:
#         gender_prefix:  Mr/Ms based on sex of person
#     """
#     print("Hello %s %s %s" % (gender_prefix, first_name, last_name))

# print(customized_hello('Maciej', 'Lubocki', 'Prof'))






# def palindrom_check(word):
#     if (len(word) % 2) != 0:
#         length = len(word)
#         counter=-1
#         for idx, letter in enumerate(word):
#             middle_letter = word[length//2]
#             if letter < middle_letter:
#              if word[idx] == word[-counter]:
#                  counter = counter-1
#             continue
#             return "true"
#         else:
#                     return "false"

# print(palindrom_check("aokajakoa"))







# def palindrom_check(word):
#     # if (len(word) % 2) != 0:
#         length = len(word)
#         counter=-1
#         for idx, letter in enumerate(word):
#             # print(idx, letter)
#             middle_letter = len(word)//2
#             if idx < middle_letter:
#                 # print(idx, middle_letter, idx < middle_letter)
#                 # print("tu ",letter, word[counter])
#                 if letter == word[counter]:
#                     # print("Counter pomniejszony", counter)
#                     counter = counter-1
#                     # print("tu ",letter, word[-counter])
#                 else:
#                     return False
#                     # print("tu ",letter, word[-counter])
#             # continue
#             else:
#                 return True
    

# print(palindrom_check("kajjak")) # powinno być True 
# print(palindrom_check("dtkajakad"))  # Powinno być True
# print(palindrom_check("robor"))  # Powinno być False





# def palindrom_check(word):
#     reversed_counter = -1
#     middle = len(word) // 2
#     for i, letter in enumerate(word):
#         if letter != word[reversed_counter]:
#             return False
#         reversed_counter -= 1
#         # doszedłęś do środka i wczęśnie litery się zgadzały
#         if i >= middle:
#             return True

# print(palindrom_check("kajjak")) # powinno być True 
# print(palindrom_check("kajak"))  # Powinno być True
# print(palindrom_check("robak"))  # Powinno być False














# print(len("potop"))


# word="potop"
# wordin=word[0]
# wordout=word[-1]
# print((wordin))
# print((wordout))

# def get_middle(s):
#   result = ''
#   length = len(s)
#   if length % 2 != 0:
#        result = s[length // 2]
#   else:
#        result = s[(length-1)//2] + s[length//2]
#        return result
# get_middle('midle')
# print(get_middle("potop"))



# print("Pokażę wszystko, co wpiszesz!")
# text = input()
# print("Oto Twój tekst: ***%s***" % text)




# def shopping(items, payment='card', shop='local shop'):
#     result = ""
#     result = result + "Idę na zakupy do %s.\n" % shop
#     result = result + "Kupię następujące rzeczy:\n"
#     for item in items:
#         result = result + " - %s\n" % item
#     result = result + "By zapłacić, używam %s." % payment
#     return result

# if __name__ == "__main__":
#     items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
#     items = items_text.split(',')
#     shopping_result = shopping(items)
#     print(shopping_result)





# def shopping(items):
#     result = ""
#     for item in items:
#         result = result + " - %s\n" % item
#     return result

# if __name__ == "__main__":
#     items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
#     items = items_text.split(',')
#     shopping_result = shopping(items)
#     print(shopping_result)



# def give_name(items):
#     result="Nazywasz sie:"
#     for item in items:
#          result = result + "%s" % item
#     return result
# if __name__ == "__main__":
#       items_text = input("Podaj proszę imie i nazwisko rozdzielone przecinkiem: ")
#       items = items_text.split(',')
#       greeting = give_name(items)
#       print(greeting)



# print("Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a")
# adult = None
# sex = input("Podaj proszę swoją płeć [M/K]: ")
# if sex == 'M':
#     age = int(input("Twój wiek? "))
#     adult = age >= 18
# elif sex == 'K':
#     print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
#     over18_yesno = input("Czy miałaś już osiemnastkę? [T/N]?")
#     adult = (over18_yesno == 'T')
# else:
#     print("Nie ma takiej płci!")
#     exit(1)
# print("Już wiem. Twoja pełnoletniość w boolean to %s" % str(adult))

# def customized_hello(first_name, last_name):
#     print("Hello %s %s!" % (first_name, last_name))

# if __name__ == "__main__":
#     customized_hello("John", "Cleese")




# import sys

# def calculator(number_1, number_2, parameter):
    
#     print("Correct result is %d!" % (result))


# if __name__ == "__main__":
#     parameter = int(input('What do you want me to do (choose appropriate number): 1. Add, 2.Deduct, 3. Multiple 4. Divide: '))
#     while not parameter <= 4:
#         if parameter >= 1:
#             print ("The integer you entered is", parameter)
#             parameter = int(input('What do you want me to do (choose appropriate number): 1. Add, 2.Deduct, 3. Multiple 4. Divide: '))
    
#     print("I will do  %d, calculation." % parameter)
    
    
#     number_1 = int(input('Please provide first number to calculate: '))
#     # while isinstance(number_1, int) == False:
#     #     number_1 = input("Please enter the value again: ")
    

    
#     number_2 = int(input('Please provide second number to calculate: '))
#     # while isinstance(number_2, int) == False:
#     #     number_2 = input("Please enter the value again: ")


#     if parameter == 1:
#         result= number_1 + number_2
#         return result
#     elif parameter == 2:
#         result= number_1 - number_2
#         return result
#     elif parameter == 3:
#         result= number_1 * number_2
#         return result
#     elif parameter == 4:
#         result= number_1 / number_2
#         return result


# Bez modułu loggin

# def calculator(number_1, number_2, parameter):
#     print("Correct result is %d!" % result)
# if __name__ == "__main__":
#     parameter = int(input('What do you want me to do (choose appropriate number): 1. Add, 2.Deduct, 3. Multiple 4. Divide: '))
#     while not parameter <= 4:
#         if parameter >= 1:
#             print ("The integer you entered is", parameter)
#             parameter = int(input('What do you want me to do (choose appropriate number): 1. Add, 2.Deduct, 3. Multiple 4. Divide: '))
#         print("I will do  %d, calculation." % parameter)
#     number_1 = int(input('Please provide first number to calculate: '))
#     while isinstance(number_1, int) == False:
#         number_1 = input("Please enter the value again: ")
#     number_2 = int(input('Please provide second number to calculate: '))
#     while isinstance(number_2, int) == False:
#         number_2 = input("Please enter the value again: ")
#     if parameter == 1:
#         result= number_1 + number_2
#     elif parameter == 2:
#         result= number_1 - number_2
#     elif parameter == 3:
#         result= number_1 * number_2
#     elif parameter == 4:
#         result= number_1 / number_2
#     print("Correct result is %d!" % result)


#Z modułem loggin

# import logging
# logging.basicConfig(level=logging.DEBUG)

# def calculator(number_1, number_2, parameter):
#     logging.info("Correct result is %d!" % result)

# if __name__ == "__main__":
#     parameter = int(input('What do you want me to do (choose appropriate number): 1. Add, 2.Deduct, 3. Multiple 4. Divide: '))
#     while not parameter <= 4:
#         if parameter >= 1:
#             logging.info("The integer you entered is", parameter)
#             parameter = int(input('What do you want me to do (choose appropriate number): 1. Add, 2.Deduct, 3. Multiple 4. Divide: '))
#         logging.info("I will do  %d, calculation." % parameter)
#     number_1 = int(input('Please provide first number to calculate: '))
#     while isinstance(number_1, int) == False:
#         number_1 = input("Please enter the value again: ")
#     number_2 = int(input('Please provide second number to calculate: '))
#     while isinstance(number_2, int) == False:
#         number_2 = input("Please enter the value again: ")
#     if parameter == 1:
#         result= number_1 + number_2
#     elif parameter == 2:
#         result= number_1 - number_2
#     elif parameter == 3:
#         result= number_1 * number_2
#     elif parameter == 4:
#         result= number_1 / number_2
#     print("Correct result is %d!" % result)





# import sys
# import logging
# logging.basicConfig(level=logging.DEBUG)

# def print_maturity(age):
#     if age >= 18:
#         logging.info("You are an adult")
#     else:
#         logging.info("You are a kiddo!")

# if __name__ == "__main__":
#     logging.debug("The program was called with this parameters %s" % sys.argv[1:])
#     logging.debug("First parameter is %s" % sys.argv[1])
#     age = int(sys.argv[1])
#     print_maturity(age)

# def number_1_input(number_1):
#     try:
#         number_1 = int(input('Please provide first number to calculate: '))
#         while isinstance(number_1, int) != False:
#             return number_1    
#     except:
#         return number_1_input("Enter correct number:")
# number_1 = number_1_input("number_1")

# print(number_1)
# print(type(number_1))


    
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

dzialania = {
    "+": add,
    "-": sub
}

dzialanie = "+"
a = 1
b = 2

print(dzialania[dzialanie](a, b))



















    


    # if len(sys.argv) < 4:
    #     exit(1)
    # first_name = sys.argv[1]
    # last_name = sys.argv[2]
    # prefix = sys.argv[3]
    # customized_hello(first_name, last_name, prefix)

    # print("to jest argument0 ", sys.argv[0])
    # print("to jest argument1 ",sys.argv[1])
    # print("to jest argument2 ",sys.argv[2])
    # print("to jest argument3 ",sys.argv[3])
    


