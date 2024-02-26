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
def checkEven(num):
    result = ''
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result

print(checkEven(4))
print(checkEven(9))

is_even = checkEven(1242454675673452345)
print(is_even)

print("Hello")
import random
randNum = random.random()

# Palindrome: EX: level, race car, mom.
# Anagrams- Two words that have same letters but have a diffeent order. EX: life and file, live and evil, god and dog.

