##### FUNCTIONS - resusable blocks of code

##### 1 Write a function to check whether a function is even or not.
# num --> function parameter
# def checkEven(num):
#     result = ''
#     if num % 2 == 0:
#         result = True
#     else:
#         result = False
#     print(result)
#
# ##### Making a function call
# checkEven(4) # 4 --> function arguments
# checkEven(9)
#
# print("Hello")
# import random
# randNum = random.random() # returns a random number


##### 2
# def checkEven(num):
#     result = ''
#     if num % 2 == 0:
#         result = True
#     else:
#         result = False
#     return result
#
# print(checkEven(4))
# print(checkEven(9))
#
# is_even = checkEven(1242454675673452345)
# print(is_even)
#
# print("Hello")
# import random
# randNum = random.random()



# Palindrome- Reads the same backwards. EX: level, racecar, mom.
# Anagrams- Two words that have same letters but have a different order. EX: life and file, live and evil, god and dog.

# efil == efil TRUE
# efil == efiil FALSE

# sort() function
# life = file
#
# sorted(efil)

def checkEven(num):
    result = ''
    if 'life' == 'file':
        result = True
    else:
        result = False
    return result

# list = ['l,' 'i,' 'f,' 'e']
# list.sort()
# print(list)
