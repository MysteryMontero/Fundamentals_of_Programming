##### LOGGING #####
# log file: Keeps track of your code.

import logging

### 5 types of information you can log: DEBUG, INFOR, WARNING, ERROR, CRITICAL
# Critical- Critical messages.
# ERROR- Error in code.
# WARNING- Something is not working right.
# INFO- Information on code.
# DEBUG- Debugging.
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

num1 = 10
num2 = 5
"""

add_res = add(num1, num2)
logging.debug(f'Add: {num1} + {num2} = {add_res}')

sub_res = subtract(num1, num2)
logging.warning(f'Subtract: {num1} - {num2} = {sub_res}')
# When changed to warning. is shows 'WARNING:root:Subtract: 10 - 5 = 5
# Warning is the default level.


# # Changing the default logging level from warning to debug:
# logging.basicConfig(level=logging.DEBUG)
#
# add_res = add(num1, num2)
# logging.debug(f'Add: {num1} + {num2} = {add_res}')
# # SHows debug error
#
# sub_res = subtract(num1, num2)
# logging.warning(f'Subtract: {num1} - {num2} = {sub_res}')
# # Shows warning error
"""

# Writing to a log file
logging.basicConfig(filename='log_sample.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s') # Prints the time stamp.

mult_res = multiply(num1, num2)
logging.debug(f'Multiply: {num1} * {num2} = {mult_res}')

div_res = divide(num1, num2)
logging.warning(f'Divide: {num1} / {num2} = {div_res}')
# Makes a separate log file and shows the output.
