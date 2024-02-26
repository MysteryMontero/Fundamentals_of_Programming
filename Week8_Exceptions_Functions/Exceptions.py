##### Exception/Error- Unwanted scenario that disrupts the flow of program.
### Logical Error- Code that doesn't make sense.
### Syntax Error- Missing code. Specific to language.

### Syntax is called compile time errors.
### Logical is called runtime exceptions.
## Normal Statements
# a = 5
# b = 0
#
# try:
#     # Critical Statement: Could state an error.
#     print(a/b) # Correct but incorrect when running the program.
# except Exception: # Makes your own error message
#     print('something wrong')
# print('end')
# Syntax would be caught by your IDE.
# Logical errors are handled by the programmer/dev.

##### 1
# try:
#     a = int(input('Enter the first number: '))
#     b = int(input('Enter the second number: '))
#     result = a / b
#     print(result) # Will print if no excepts/errors are met.
# except ZeroDivisionError as e:
#     print('Something went wrong-', e)
# except ValueError as e:
#     print("Something went wrong-", e)
# except Exception as e:
#     print("Something went wrong-", e)
# print('End')

##### 2 ELSE BLOCK
# try:
#     a = int(input('Enter the first number: '))
#     b = int(input('Enter the second number: '))
#     result = a / b
# except ZeroDivisionError as e:
#     print('Something went wrong-', e)
# except ValueError as e:
#     print("Something went wrong-", e)
# except Exception as e:
#     print("Something went wrong-", e)
# else:
#     print(result) # else block code only run if no errors inn the try block.
# print('End')

##### 3 FINALLY BLOCK
# try:
#     print("Connection opened")
#     a = int(input('Enter the first number: '))
#     b = int(input('Enter the second number: '))
#     result = a / b
# except ZeroDivisionError as e:
#     print('Something went wrong-', e)
# except ValueError as e:
#     print("Something went wrong-", e)
# except Exception as e:
#     print("Something went wrong-", e)
# else:
#     print('From_else: ', result)
# finally:
#     print("Connections closed") # used for the code that needs to be executed whether an error is found or not.
# print('End')

##### 4
numbers = [1, 2, 3, 4, 0, 5, 6]

for num in numbers:
    try:
        result = 10/num
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)

