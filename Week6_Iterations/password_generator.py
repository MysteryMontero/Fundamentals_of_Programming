# ### PASSWORD GENERATOR
# Passwords have letters, digits, and symbols

import random

letters = list('abcdefghijklmnopqrstuvwxyz')
digits = list('0123456789')
symbols = ('!@#$%^&*()')

num_letters = int(input('How many letters do you want? '))
num_digits = int(input('How many digits do you want? '))
num_symbols = int(input('How many symbols do you want? '))

password_chars = []

for letter in range(0, num_letters):
    password_chars.append(random.choice(letters))

for digit in range(0, num_digits):
    password_chars.append(random.choice(digits))

for symbol in range(0, num_symbols):
    password_chars.append(random.choice(symbols))

print(password_chars) # Displays them in order: Letters, Digits, Symbols.

random.shuffle(password_chars) # Randomly shuffles them around
print(password_chars)

password = ''.join(password_chars) # Joins the characters together
print(password)

### HOMEWORK 6 ####
# 1. Write a program to print a list of all prime numbers till a given target number.

# rows = int(input('Number of rows: '))
#
# for num in range(1, rows + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

