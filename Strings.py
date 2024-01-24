# Do not use reserved keywords for variable names
'''
print ('Hello World!')
print(help('keywords'))

# Try to avoid multiple variable declaration simultaneously
a = b = c = 10 # Shortcut for below: works but not recommended
a = 10
b = 10
c = 10
print(a,b,c)

# Statement vs Expression
x = 47 # statement
y = x + 10 # expression

# TYPE Convversion --> to change the data type of a variable#
# Convert floats and numeric strings to an int
print(int("20"))
print("30")
print(type(int("20")))
print(int(14.21))

# print(int("20.24")) # errors out out because it expects whole numbers inside codes. No ""
print(int(float("20.24")))

## STRINGS ##
# 3 ways to create a string - using either single, double, or triple quotes: '', "", ''''''
first_name = 'Jane'
last_name = "Doe"
# address = ''''''

job = "Physican's Assistant" # Recomended to use double quotes for strings

## STRING FUNCTIONS
# len() --> Returns the number of characters in a string
print(len("Hello")) # 5 characters

# upper and lower --> convert the string to upper and lowercase
print("Hello".upper())

# String concatenation - adding up strings
first_name = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name) # The middle represents a space
age = "24"
print(first_name + ' ' + last_name + ':' + ' ' + str(age)) # age is not an integer, so we need to make it a string

# String Multiplication - can multiply a string with an int
print("hello"*3)

# Access string characters - a string is just a sequence of characters
# Index = 1 2 3 4
# Last index = length - 1
name = "Jane Doe"
print(name[2])
# print(name[8]) # throws index out of bound error

# Retrieving the character ata  given index
print(name.index('o')) # returns 6
print(name.index('e')) # returns the index of first occurrence
'''