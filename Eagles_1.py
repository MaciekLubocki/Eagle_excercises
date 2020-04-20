numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

for number, item in enumerate(numbers):
    if val[number] < 10:
       numbers[number] = 10
    else:
        numbers[number] = round(number, -1)
        
print(numbers)


for number, item in enumerate(list):
       if number in item < 10:
       item = replace_all(...)
       list[idx] = item



for item in list:
    if "foo" in item:
        item = replace_all(item, replaceDictionary)
        list[item] = item
        print item



# for number in numbers:
#     if number < 10:
#        numbers[number] = 10
#     else:
#         numbers[number] = round(number, -1)
        
# print(numbers)


x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))


# Znajdź średnią zmodyfikowanej listy
# Twoim zadaniem jest zmodyfikowanie listy przypisanej do zmiennej numbers w taki sposób, aby każdy jej element zaokrąglić do pełnej dziesiątki. Postaraj się nie tworzyć nowej listy będącej zmodyfikowaną listą numbers, lecz zmodyfikować listę numbers.
# Po zaokrągleniu każdego elementu listy numbers, pozbądź się jej największego oraz najmniejszego elementu, a następnie do zmiennej mean_number przypisz średnią z ostatecznie zmodyfikowanej listy.
# Podsumowując:
# zaokrąglij każdy element numbers do pełnej 10 (np. 5 -> 10, 32 -> 30)
# znajdź, a następnie pozbądź się największego oraz najmniejszego elementu zmodyfikowanej listy
# policz średnią z ostatecznie zmodyfikowanej listy numbers i przypisz ją do zmiennej mean_number