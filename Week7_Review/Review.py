# for i in range(11):
#     if i == 6:
#         break
#     else:
#         print(i)

## Continue
# for i in range(11):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

#### Problem 1
# total = 0
# count = 0
#
# input_str = input('Enter a string with numbers, letters, and symbols: ')
#
# for char in input_str:
#     if char.isdigit():
#         total = total + int(char)
#         count = count + 1
# avg = total/count
# print(f'Sum: {round(total, 2)}, Average: {avg}')

#### Problem 2
# Write a program to print the number of digits, letters, and symbols in a given string.
# Ex: random289$18@str849ing6
# Output: Digits: 9, Letters: 12, Symbols: 2 isdigit, isalpha, is...

# string = 'random289$18@str849ing6'
# digit = 0
# letter = 0
# symbol = 0
#
# for i in string:
#     if i.isdigit():
#         digit = digit + 1
#     elif i.isalpha():
#         letter = letter + 1
#     else:
#         symbol = symbol + 1
#
# print("Digits:", digit)
# print("Letters:", letter)
# print("Symbols:", symbol)

### Problem 3
# target = random.random(1, 100)
# user_guess = input ('')
# target = 13
#
# guess = input("Enter a number between 1 and 20: ")
# if guess > 13 or guess < 13:
#     print('Nope')
# elif guess == 13:
#     print('Yes')
# else:
#     print('Nope')









##### Programming Final Review #####
Quick Sort:
You want to find the median value…or median values, of the given list. EX List: [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]
1.	Take the list given and grab the first, middle, and last value from it. EX: [31, 92, 28]
2.	Find the medium between the 3 values. EX: [31]
3.	Find what’s less than, equal to, and greater than 31 in the main list and divide it into 3 lists. EX: list1 < 31: [18, 18, 3, 11, 28], list2 = 31: [31], list3 > 31: [72, 79, 92, 44, 56, 41]
4.	Repeat the same steps for list1 and list3. Since list2 has only one value, it’s done.
5.	Continue to break the lists down but by bit until you can't no further.
6.	In the end, the list will be sorted in proper order from least to greatest. As you break it down in a tracing tree, the numbers from left to right will appear in order.
##### QUICK SORT #####
# Using the same list
# Step 1: Find the median value
# Step 2: Create 3 lists
#       a: First list: has all the values < median values
#       b: Second list: has all the values = median values
#       c: Third list: has all the values > median value
# Step 3: Repeat step 1 and step 2 for first and third list until there is only one element left in each list.

# [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]

# median(list[0], list[len(list)//2], list[-1])
#   1st value     middle value     last value

# Step 1: (take the first, middle, and last value of the list):
# median([31, 92, 28]) = 31 is the median of the three.

# Step 2: Compare 31 to the main list below:
# list1 < 31: [18, 18, 3, 11, 28]
# list2 = 31: [31]
# list3 > 31: [72, 79, 92, 44, 56, 41]

# Step 3: Repeat for list 1
# [18, 18, 3, 11, 28] = 18 is median
# list1 < 18: [3, 11]
# list2 = 18: [18, 18]
# list3 > 18: [28]

# Repeat AGAIN
# Step 1: [3, 11] divide by 2 (just duplicate the last element) = [3, 11, 11] median = 11
# list 1 < 11: [3]
# list 2 = 11: [11]
# list 3 > 11:

# Repeat for list 3
# [72, 79, 92, 44, 56, 41]
# Step 1: [72, 44, 41] = 44 is the median
# So 44 is the median because we take the number of variables (6) and divide it by 2 = 3.
# So we go to index 3 which is 44.

# list1 < 44: [72, 79, 92, 56]
# list2 = 44: [44]
# list3 > 44: [41]

# Repeat...AGAIN
# [72, 79, 92, 56]
# Step 1: [56, 92, 92] = 92 is the median
# list 1 < 92:
# list 2 = 92: [92]
# list 3 > 92: [72, 79, 56]

# Then take this bloody list and find the median
# [72, 79, 56] = 72 is the median
# list 1 < 72: [79]
# list 2 = 72: [72]
# list 3 > 72: [56]

Recursion:
Works with both memoization and tabulation.
Best used with the Fibonacci series: [1 1 2 3 5 8 13 21]
I figured out how this code works. Let's do 3 as an example. The index is at 3.
1.	Both the i's are 3. It's not subtracting mathematically; it's going down an index.
2.	So 3-1 is going down to 2 and 3-2 is going down to 1. It may look like it, but it's not mathematical. 2+1 = 3, which is the next value in the fib sequence.
3.	Then it adds the next 2 numbers, which are 2 and 3, which equal 5.
4.	5-1 goes down to 3 & 5-2 goes down to 2. So 3+2 = 5, the next value.
5.	Then is shifts to add 3 + 5 to 8: 8-1 goes down to 5 & 8-2 goes down to 3, 5+3 = 8.
6.	In hindsight, i-2 comes first and i-1 comes second. You take the value 8, go down two times to get 3, then go down 8 one time to get 5, and add 3 and 5 together to make 8. That explains the subtractions.

Memoization:
Method of storing temporary results of sub-problems to use later.
So for example: fib(0): 0, and we store that. when doing a tracer tree, we don’t have to put that branch anymore.

Tabulation:
# Look at the graph and put the values of each branch in the chart accordingly.
# For example, A[2]B[0] would fall down to A column 2 and B column 0, and /0 was the answer, so the answer in the box is 0.
# The one with X were not values in the chart.
# 	B:  	a   b   c   d  /0
#       		0   1   2   3   4
# A: 	b    0: 	2   2   X  X  X
# 	d    1: 	1   1   1   1   X
#	\0   2: 	0   0   0   X   0

Multiple Choice:
Break: Breaks a continuing loop. Allows you to exit a loop when endpoint is met.
EX: If the value is 3, the loop will go up to 3 and then break off/stop.

Continue: Skips the value displayed and continues after it.
EX: for var in "Geeksforgeeks":
    if var == "e":
        continue
    print(var)
(All ‘e’s in the phrase will not be shown.)


Lists: A list of values. “[]”
EX: countries = ['Canada', 'France', 'Mexico', 'Germany', 'France', 'USA', 'Thailand', 'Denmark']

Tuples: Like a list, but cannot me modified, updated, or can add or remove an element. “()”
EX: tuple1 = (12, 234, 4255, 23) # Useful for inches, cm.

Sets: Like lists but do not allow duplicates or guarantee correct order. “{}”
EX: countries = {'Russia', 'China', 'Japan', 'Sudan', 'Japan'}
(Does not print ‘Japan’ twice.)

Try: Lets you test code for errors.
Except: Lets you handle the errors in a try code.
EX: except ZeroDivisionError as e:
Print ('Something went wrong-', e)
Else: Executes the code when all errors are taking care of.
Finally: Executes the code regardless of any errors are found or not.
EX: # try:
#     print("Connection opened")
#     a = int(input('Enter the first number: '))
#     b = int(input('Enter the second number: '))
#     result = a / b
# except ZeroDivisionError as e:
#     print('Something went wrong-', e)
# except ValueError as e:
#     print("Something went wrong-", e)
# except Exception as e:
#     print("Something went wrong-", e)
# else:
#     print('From_else: ', result)
# finally:
#     print("Connections closed") # used for the code that needs to be executed whether an error is found or not.
# print('End')


Type of Errors:
Exception/Error- Unwanted scenario that disrupts the flow of program.
Logical Error- Code that doesn't make sense. EX: 1+2 = Fish
Syntax Error- Missing code. EX: print “Jim”) (Missing a ‘(‘ in the front)
Name Error- The name of a value doesn’t match anything else. EX: Koby (Nothing else in the code is connected to this name.)
Division by Zero Error- Dividing by zero. EX: 10/0
Value Error- The value is not correct. Occurs when a function is called with the proper argument type but with the wrong value. EX: a=10 b=Tree (Value Error)
Index Error- An item from a list that is outside the list and cannot be accessed. EX: [A, B, C] | print index 3 (There is no item in index 3.)
Key Error- Trying to access a key word that isn’t in a dictionary. EX: dict: [Kevin, Jim, Rodney] | dict: [Michael] (Can’t access Michael because it’s not in the dictionary.)

Parameter: The variable listed inside the ‘()’ in the function definition.
EX: def checkEven(num) | num is the parameter.
Argument: The value that is sent when it is called.
EX: print(checkEven(4)) | 4 is the argument.

Lambda: Makes a function smaller and easier, but can only have one expression.
EX: square_num1 = lambda a: a * a
print(square_num1(5)) # Same result; 5^2
EX2: add_nums = lambda a, b: a + b
print(add_nums(4, 5)) # Adds a & b, which is 4 + 5

IIFE: Immediately Invoked Function Expressions. Even shorter line of code used for only one-time code.
EX: print((lambda name: f"Hello {name}!")('Jane')) | That’s the entire code.

Filter: Picks out certain things from a list.
EX: # nums = [3, 2, 6, 8, 4, 6, 2, 9]
# def is_even(n):
#     return n % 2 == 0
# even_nums = filter(is_even, nums)
# print(list(even_nums)) # Prints all even numbers from the list
Map: Changes the values in a given list.
EX: # nums = [3, 2, 6, 8, 4, 6, 2, 9]
# def double_num(n):
#     return n * 2
# doubles = map(double_num, nums)
# print(list(doubles)) # Multiplies all numbers in the list by 2
Reduce: Used when wanting to obtain a single value from a list. Like the sum of all #'s in a list, we get one value.
EX: # nums = [3, 2, 6, 8, 4, 6, 2, 9]
# from functools import reduce
# def add_all(a, b):
#     return a + b
# total_sum = reduce(add_all, nums)
# print(total_sum) # The total sum of nums list, which is 40

Recursion: A common mathematical concept where a function calls itself. Memoization and Tabulation are different ways of recursion. Usually tied with the Fibonacci series.
Memoization: Storing the results of sub problems and using them later. You store each fib in a dictionary. You don't need repeating branches once you have the solution.
Tabulation: Solve the problem from the bottom up.

Modules:
Standard: In-built/already built in. EX: import random. Random, math, & reduce are all standard modules.
External: Not part of a language, will have to install before importing. EX: Pandas, NumPy.
Custom: Module that is built by developers for their specific needs.

Alias: Names used for module names when importing. Transports from one file to the other.
EX: # import find_index_module as fim | The name ‘fim’ is used for transporting the code to the file ‘find_index_module’

API: Application Program Interface. Interfaces like Facebook and Twitter on how they track each individual account.

File Handling:
With files (3):
Reading: Reads the code in a different file. ‘r’
Writing: Writes in a different file. ‘w’
EX: # with open('write_test.txt', 'w') as file_obj: # 'w' represents write.
# file_obj.write('Writing') # Makes a new file 'write_test' and writes 'Writing' in it.
Append: Adds on a new word. ‘a’

With Open: Opens the file, supports the context manager. Used along with alias and APIs.

CSV module: The most common import and export format for spreadsheets and databases. An API file.
EX: import CSV.
