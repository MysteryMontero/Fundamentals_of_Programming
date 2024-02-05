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
'''
grade = int(input('Enter your grade: '))

if grade < 60:
    print('FAILURE')
else:
    if grade < 70:
        if grade < 63:
            print('D-')
            