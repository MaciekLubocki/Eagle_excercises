# dice_numbers = {}
# L = [1,2,3,4,5,6]

# for rzut in range(1,6):
#     s = set(L)
#     edgeCase = rzut/2
#     if L.count(edgeCase) < 2:
#           print (edgeCase, edgeCase)
#     s.remove(edgeCase)
#     for i in s:
#         diff = rzut-i
#         if diff in s: 
#              dice_numbers[rzut]=(i, diff)



# print(dice_numbers)




def find_pairs(L,sum):
    s = set(L)
    edgeCase = sum/2
    if L.count(edgeCase) ==2:
        print (edgeCase, edgeCase)
    s.remove(edgeCase)      
    for i in s:
        diff = sum-i
        if diff in s: 
            print (i, diff)

L = [2,45,7,3,5,1,8,9]
sum = 10          
find_pairs(L,sum)



# def sumToK(lst):
#     k = 0  # <- define the k here
#     d = {} # build a dictionary 

# # build the hashmap key = val of lst, value = i
# for index, val in enumerate(lst):
#     d[val] = index

# # find the key; if a key is in the dict, and not the same index as the current key
# for i, val in enumerate(lst):
#     if (k-val) in d and d[k-val] != i:
#         return True

# return False



# for name in names:
#     litera = name[0]    
#     if litera in name_dict:  # to sprawdza czy juz masz taki klucz - np literę P
#          name_dict[litera].append(name)
#     else:  # jesli takie slownika jeszce ni ma to po prostu tworzysz nowa wartosc czyli liste z aktualnym imieniem
#         name_dict[litera] = [name]





# def find_pairs(L,sum):
#     s = set(L)
#     edgeCase = sum/2
#     if L.count(edgeCase) ==2:
#         print (edgeCase, edgeCase)
#     s.remove(edgeCase)      
#     for i in s:
#         diff = sum-i
#         if diff in s: 
#             print (i, diff)



# sum = 6          
# find_pairs(L,sum)