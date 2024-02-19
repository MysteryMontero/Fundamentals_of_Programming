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
target = 13

guess = input("Enter a number between 1 and 20: ")
if guess > 13 or guess < 13:
    print('Nope')
elif guess == 13:
    print('Yes')
else:
    print('Nope')