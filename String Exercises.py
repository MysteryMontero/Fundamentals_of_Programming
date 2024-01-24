# Question 1: Take an input string from the user and create a new string using first, middle, and last characters
# STEPS:
# 1. Take the use input and set it to a variable
user_string = input('Please enter a string: ')
print(user_string)
# 2. Get the first character using index 0 and store it in a variable
first_char = user_string[0]
# 3. Get the last character using index -1 and store it in a variable
last_char = user_string[-1]
# 4. To get middle character: Find lengh of sring, find mid index using length/2, and get character at mid index using (mid-index)
str_length = len(user_string)
mid_index = int(str_length/2)
print(mid_index)

mid_char = user_string[mid_index]
# 5. Concatenate a, b, c
new_str = first_char+mid_char+last_char
print(new_str)

