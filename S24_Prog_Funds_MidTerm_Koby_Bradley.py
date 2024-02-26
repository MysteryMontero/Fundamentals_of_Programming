# 1. using a while loop, print odd numbers until a given number
# rows = int(input('Number of rows: '))
#
# for num in range(1, rows + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
# FAILED

# 2.
# fruits = ["banana", "orange", "apple", "kiwi", "apple", "apple", "grapes"]
# i = 0
# for i in fruits:
#      if i <= 1:
#           print("Fruits")
#      else:
#           print('Nothing')
# FAILED


# 3.
# import random
#
# user_move = input('heads or tails: ')
# rand_num = round(random.random(), 1)
# comp_move = ''
#
# if rand_num >= 1:
#     comp_move = 'heads'
# else:
#     comp_move = 'tails'
#
# result = ''
# if user_move == 'heads':
#     if comp_move == 'heads':
#         result = 'You Win...yay'
#     else:
#         result = 'You Lose!'
# elif user_move == 'tails':
#     if comp_move == 'tails':
#         result = 'You Win...yay'
#     else:
#         result = 'You Lose!'
#
# print(f'You picked {user_move}. Computer picked {comp_move}. {result}')
# SUCCESS

# 4.
# List1 = [12, 75, 150, 180, 145, 525, 50]
# if List1 > 500:
#      break
# elif List1 % 5:
#      print(List1)
# FAILED

# 5.
# for i in range(0, 9):
#      for j in range(0, i * 1):
#           if j % 2 == 0:
#              print(j, end=' ')
#      print()
# FAILED
