
##### RECURSION 1 #####
# def sayHello(name):
#     print(f"Hello {name}!")
#
# def userDetails():
#     user_name = input("Enter a name: ")
#     sayHello(user_name)
#     user_city = input("Enter a city: ")
#     print(f"You are from {user_city}")
# userDetails() # The starting point


##### 2 #####
# def test1(n):
#     if(n > 0):
#         print("Printing the value. ")
#         print(n)
#         print("Calling the function")
#         test1(n-1) # Subtracts from n every time.
# test1(3) # Starts from 3 and subtracts 1 until its no longer greater than 0.


##### 3 #####
# def test2(n):
#     if(n > 0):
#         print("Calling the function")
#         test2(n - 1) # Because its a function, it keeps printing Calling until n is less than 0.
#         print("Printing the value. ")
#         print(n)
# test2(3)


##### 4 #####
# def test1(n): ### HEAP MEMORY
#     if(n > 0):
#         print(n)
#         test1(n - 1)
# test1(3) # Counts down to 1.
#
#
# def test2(n): # STACK MEMORY
#     if(n > 0):
#         test2(n - 1)
#         print(n)
# test2(3) # Goes down then reverses and starts counting up.



##### 5 FIND THE FACTORY OF A NUMBER #####

### WHAT IS A FACTORY? ###
# Formula: n! = n*(n-1)!
# 5! = 5*4*3*2*1 = 120 also known as 5*4!(24) = 120
# 4! = 4*3*2*1 = 24 also 4*3! = 24
# 3! = 3*2*1 = 6 also 3*2! = 6
# 2! = 2*1 = 2
# 1! = 1
# 0! = 1

# def findFactorial(n): # CODE FOR FINDING FACTORIAL NUMBERS
#     if(n < 0): # THIS IS FOR ANYTHING BELOW 0
#         print("Please provide a positive number")
#         return
#     elif (n <= 1): # THIS IS FOR EITHER 0 OR 1
#         return 1
#     else:
#         return n * findFactorial(n-1) # FACTORIAL CODE
# factorial = findFactorial(5)
# print(factorial)


### 6 FIBONACCI SERIES ###
# 1 1 2 3 5 8 13 21 # YOU ADD THE NEXT TWO NUMBERS AND GET THE NEXT NUMBER.
# 8 + 13 = 21

# fibSeries(5)
# should print 1 1 2 3 5


# def fibSeries(n):
#     if(n < 0):
#         print("Please provide a positive number")
#         return
#     elif (n <= 1):
#         return 1
#     else:
#         return n * fibSeries(n-1)
# factorial = fibSeries(5)
# print(factorial)


##### SORTING THE LIST OF NUMBERS #####
##### BUBBLE SORT #####

# list = [31,18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]

# Bubble Sort: first 2 numbers. 18 is smaller than 31, so 18 will go first. Then 31 and 72. 31 is smaller so it stays.
# 1. 18, 31
# 2. 18, 31, 72
# 3. 18, 31, 72, 79
# Result = 18, 31, 72, 3, 18, 79, 11, 44, 56, 28, 92

# Result will be the largest number (92) being at the end.

# Start the same process again, and you have the second-largest number at the second end, which is 79.
# Result = 18, 31, 3, 18, 72, 11, 44, 56, 28, 79, 92.

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
#   1st values     middle value     last value


# Step 1: (take the first, middle, and last value of the list):
# median([31, 92, 28]) = 31 is the median of the three.

# Step 2:
# list1 < 31: [18, 18, 3, 11, 28]
# list2 = 31: [31]
# list3 > 31: [72, 79, 92, 44, 56, 41]



# Step 3: Repeat for list 1
# [18, 18, 3, 11, 28] = 18 is median
# list1 < 18: [3, 11]
# list2 = 18: [18, 18]
# list3 > 18: [28]

# Repeat AGAIN!
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


##### IN CODE FORM #####
##### YES, IT IS COMPLICATED, SO REMEMBER IT #####
# import statistics
#
# def quickSort(num_list):
#     if len(num_list) <= 1:
#         return num_list
#     else:
#         # find median
#         median_value = statistics.median([num_list[0],
#                                           num_list[len(num_list)//2],
#                                           num_list[-1]]
#                                          )
#         left_list = []
#         middle_list = []
#         right_list = []
#         for i in num_list:
#             if i < median_value:
#                 left_list.append(i)
#             elif i > median_value:
#                 right_list.append(i)
#             else:
#                 middle_list.append(i)
#         return(quickSort(left_list) + middle_list + quickSort(right_list))
# sorted_list = quickSort([31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28])
# print(sorted_list)


# Memoization: Storing temporary results.
# Tabulation: Loops.

