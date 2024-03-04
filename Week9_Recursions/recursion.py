
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

### WHAT IS A FACTORY?
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
