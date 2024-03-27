# def square_num(a):
#     return a * a
# print(square_num(5)) # This outputs 5^2.
#
# square_num1 = lambda a: a * a # If you want 2 #'s, it would be a, b:
# print(square_num1(5)) # Same result; 5^2
#
# add_nums = lambda a, b: a + b
# print(add_nums(4, 5)) # Adds a & b, which is 4 + 5.
#
# hello_user = lambda name: f"Hello {name}!"
# print(hello_user('John')) # Prints Hello John!
#
# # WRITE A LAMBDA THAT CHECKS IF A NUMBER IS EVEN OR ODD
# # SHOULD PRINT AN EVEN NUMBER IF IT IS EVEN, OTHERWISE PRINT ODD NUMBER
# check_even = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
# print(check_even(5)) # It really works
#
# # Lambda honestly makes it easier
#
#
# ##### IMMEDIATELY INVOKED FUNCTION EXPRESSIONS or IIFEs #####
# # We are not assigning a function name to IIFEs.
# # Mainly used for one time code.
#
# print((lambda name: f"Hello {name}!")('Jane')) # IIFE version of Hello Jane!
#
# print((lambda num: num + 5)(5)) # Prints num + 5
#
#
# ### HIGHER ORDER FUNCTIONS ###
# # 3 common functions: filter, map, reduce
#
# ### FILTER ###
# # Filter picks out certain things from the list.
# nums = [3, 2, 6, 8, 4, 6, 2, 9]
# def is_even(n):
#     return n % 2 == 0
# even_nums = filter(is_even, nums)
# print(list(even_nums)) # Prints all even numbers from the list
#
#
# even_nums1 = filter(lambda num: num % 2 == 0, nums)
# print(list(even_nums1)) # Prints even numbers in lambda form
#
# ### MAP ###
# # Used in to perform some operation on every element in a list.
# # Map for every element we want to do something with it.
#
# def double_num(n):
#     return n * 2
# doubles = map(double_num, nums)
# print(list(doubles)) # Multiplies all numbers in the list by 2
#
#
# doubles1 = map(lambda n: n * 2, nums)
# print(list(doubles1)) # Same outcome in lambda form
#
# # Map EX2:
# cities = ['New York', 'Miami', 'Phoenix', 'Columbus', 'Pittsburgh']
# # Using map and lambda, return a list with the lengths of all the cities
#
# broad = map(lambda n: len(n), cities)
# print(list(broad)) # Prints the number of values in each city name
#
# ### REDUCE ###
# # Used when we want to obtain a single value from a list
# # Like the sum of all #'s in a list, we get one value
#
# # sum -> Accumulator
# # sum = 0
# # for n in nums: # Current value
# #       sum = sum + n
# #   return sum
#
# from functools import reduce
# def add_all(a, b):
#     return a + b
# total_sum = reduce(add_all, nums)
# print(total_sum) # The total sum of nums list
#
# total_sum1 = reduce(lambda a, b: a+b, nums)
# print(total_sum1) # Same outcome in lambda form


### HOMEWORK HEAD START ###
# 1. Write a lambda function that takes 2 arguments and returns the product of those 2 arguments.
square_num1 = lambda a, b: a * b
print(square_num1(5, 4))

# 2. Write a lambda IIFE that takes 2 numbers as parameters and returns the difference between them.
print((lambda a, b: a - b)(5, 4)) # Prints a - b

# 3. Using filter and lambda write a function that returns all the numbers greater than 5
# from a given list.
nums = [3, 2, 6, 8, 4, 6, 2, 9]
even_nums1 = filter(lambda nums: nums > 5, nums)
print(list(even_nums1)) # Prints even numbers in lambda form

# 4. Write a lambda function that returns num/5 if a given number is greater than 10.
# Otherwise, returns num + 5
check = lambda nums: nums / 5 if nums > 10 else nums + 5
print(check(12))

# 5. Using map and lambda, write a function to multiply every number in a list by 2.
doubles = map(lambda n: n * 2, nums)
print(list(doubles))

# 6. Using map, filter and reduce:
# i) Find the odd numbers from a given list
# ii) Square each odd number
# iii) Sum of squared odd numbers
nums = [3, 2, 6, 8, 4, 6, 2, 9]
bloop = list(filter(lambda num: num % 2 != 0, nums))
print(bloop) # Prints odd numbers in lambda form

bloop = list(map(lambda n: n * n, bloop))
print(bloop) # Same outcome in lambda form

from functools import reduce
bloop = reduce(lambda a, b: a+b, bloop)
print(bloop)