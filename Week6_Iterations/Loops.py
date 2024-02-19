# ### LOOPS ###
# # Iterations means repeating the same thing; Loops.
# ##### WHILE LOOP
#
# x = 1
# while x < 5: # loop variable- x
#     print(x)
#     x = x + 1 # Adds 1 to every loops. Can also do x += 1
#
# y = 1
# while y <= 10:
#     print(y)
#     y = y + 1
#
#
#
# # Roshambo
# import random
#
# # rand_num = random.random() # Ranges from zero to one
# # print(round(rand_num, 2)) # Rounds to the nearest tenth. 2 = 0.11. 3 = 0.111. 4 = 0.1111.
#
# user_choice = 'yes'
#
# while user_choice.lower() == 'yes': # Lower converts to lowercase
#     user_move = input('Pick your move - rock/paper/scissors: ')
#     rand_num = round(random.random(), 2)
#     comp_move = ''
#
# if rand_num >= 0 and rand_num < 1/3:
#     comp_move = 'rock'
# elif rand_num >= 1/3 and rand_num < 2/3:
#      comp_move = 'paper'
# else:
#     comp_move = 'scissors'
#
# result = ''
# if user_move == comp_move:
#     result ='Tie.'
# elif user_move == 'rock':
#     if comp_move == 'scissors':
#         result = 'You Win...yay'
#     else:
#         result = 'You Suck!'
# elif user_move == 'paper':
#     if comp_move == 'rock':
#         result = 'You Win...yay'
#     else:
#         result = 'You Suck!'
# elif user_move == 'scissors':
#     if comp_move == 'paper':
#         result = 'You Win...yay!'
#     else:
#         result = 'You Suck!'
# print(f'You picked {user_move}. Computer picked {comp_move}. {result}')
#
# user_choice = input('Do you want to play again? Enter yes or no: ')
#
# print('Thank You')
#
#
# #### BREAK
#     x = 1
#     while x <= 10:
#         if x == 3:
#             break
#         print(x)
#         x = x + 1
#
#
# #### CONTINUE
# x = 1
# while x <= 10:
#     if x == 3:
#         continue
#     print(x)
#     x+=1
#
#
# ####################### FOR LOOPS
# nums = [1, 2, 3, 4, 5] # Prints out list.
#
# for num in nums:
#     print(num + 10)
#
#
# ####################### RANGE
# # range(starting value, ending value, step)
# for i in range(1, 10, 2): # range- starting value is 0; ending value is not included.
#     print(i)
#

####################### Find the sum of first 100 natural numbers
# sum = 0
#
# for i in range(101): # 1+2+3+4+5...
#     print('sum: ', sum)
#     print('i: ', i)
#     sum = sum + i
#     print('after adding: ', sum)
#
# print(sum)

#
# ########### MULTIPLICATION TABLE
# num = int(input('Enter a number: '))
# for i in range(1, 11):
#     print(f'{num} * {i}: ', num * i)
#
#
# ############### NESTED LOOPS
# for num in [1, 2, 3]:
#     for letter in 'abc':
#         print(num, letter) # Prints a letter for each number.
#
# rows = int(input('Number of rows: '))
#
# for i in range(1, rows + 1): # Makes rows of numbers.
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
#
# rows = int(input('Number of rows: '))