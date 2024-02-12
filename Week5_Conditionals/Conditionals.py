'''
## if-else
height = int(input('Enter your height in cms: '))
if height > 120:
    print('Can Ride')
else:
    print('Can\'t Ride') # \ makes code ignore apostrophe in can't.


### Nested if-else # Permits multiple if-else variables
height = int(input('Enter your height in cms: '))
if height > 120:
    age = int(input('Enter your age: '))
    if age <=18:
        print('Ticket is $7')
    else:
        print('Ticket is $12')
else:
    print('Cannot Ride')

## Nested if-else with elif and multiple conditions
height = int(input('Enter your height in cms: '))
total_bill = 0

if height > 120:
    print('Can Ride')
    age = int(input('Enter your age: '))
    if age < 12:
        ticket_price = 5
        print('Ticket is $5')
    elif age >= 12 and age < 18: # Gives and variable. Splits into 3 different directions.
        ticket_price = 7
        print('Ticket is $7')
    elif age >= 45 and age < 55:
        ticket_price = 0
        print('Ticket is $0')
    else:
        ticket_price = 12
        print('Ticket is $12')

    want_photos = input("Do you want photo taken? Enter Y/y or N/n: ")

    if want_photos == "Y" or want_photos == "y":
        total_bill = ticket_price + 3
    print(f'The total bill is {total_bill}')
else:
    print('Cannot Ride') # The line up is important as it connects to certain ifs.


grade = int(input('Enter your grade: '))

if grade < 60:
    print('FAILURE')
else:
    if grade < 70:
        if grade < 63:
            print('D-')


#####

# 1. Write a program that takes a digit as an input and returns the corresponding word.
# Example: Input is 1 and program returns “one"
# Method 1: Using 3 Rule Force
digit = int(input('Enter a number: '))

if digit == 0:
    print('Zero')

    # For digit 1
elif digit == 1:
    print("One")

    # For digit 2
elif digit == 2:
    print("Two ")

elif digit == 3:
    print("Three")

elif digit == 4:
    print("Four")

# Method 2: Using Dictionary
dict1 = {
    0: 'Zero',
    1: 'One',
    2: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

num = int(input('Enter a number 0-9: '))

print(dict1[num])

# Method 3: Using a List
list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num = int(input('Enter a number 0-9: '))
print(list1[num])

'''
# 2. Simulate the “Rock Paper Scissors” game.
import random
# rand_num = random.random() # Ranges from zero to one
# print(round(rand_num, 4)) # Rounds to the nearest tenth. 2 = 0.11. 3 = 0.111. 4 = 0.1111.

user_move = input('Pick your move - rock/paper/scissors: ')
rand_num = round(random.random(), 2)
comp_move = ''

if rand_num >= 0 and rand_num < 1/3:
    comp_move = 'rock'
elif rand_num >= 1/3 and rand_num < 2/3:
     comp_move = 'paper'
else:
    comp_move = 'scissors'

result = ''
if user_move == comp_move:
    result ='Tie.'
elif user_move == 'rock':
    if comp_move == 'scissors':
        result = 'You Win...yay'
    else:
        result = 'You Suck!'
elif user_move == 'paper':
    if comp_move == 'rock':
        result = 'You Win...yay'
    else:
        result = 'You Suck!'
elif user_move == 'scissors':
    if comp_move == 'paper':
        result = 'You Win...yay!'
    else:
        result = 'You Suck!'
print(f'You picked {user_move}. Computer picked {comp_move}. {result}')
# 3. Write a program that takes year as input and checks whether the given year is leap or not.
yeah = 2020
print(yeah%4) # Percent(%) gives the remainder

if yeah%4 == 0 and yeah%100 != 0 or yeah%400 == 0:
    print('Leap Year')
else:
    print('Not Leap')

'''
# 4. Write a program that simulates the logic shown in the below flowchart
print('Welcome to Treasure Island. Your mission is to find the booty. And then give it to me as payment. Tax rate.')
dir1 = int(input('Where should you go first? left or right: '))

if dir1 == 'left':
'''
