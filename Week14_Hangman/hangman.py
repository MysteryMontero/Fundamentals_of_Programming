'''
##### READ MODE #####
### Open Command ###
# open command
# with open --> context manager (More recommended)

# 1. Using the open command
# With files, there are 3 modes: Read, Write, Append
file_obj = open('sample_text', 'r') # 'r' means for reading.
# default mode is 'r'

print(file_obj.name) # Displays 'sample_text,' the name of the file.
print(file_obj.mode) # Checks the mode, shows 'r'

# Using an open command, you really want to close the command.
file_obj.close() # Used to close the file.
'''

# 'with open' is safer than 'open'
# 'with open' supports context manager.
# Keep the below code line open for all other code.
with open('sample_text', 'r') as file_obj: # The reference to file_obj
    # print(file_obj.name) # Prints 'sample_text'
    # print('inside the with open: ', file_obj.closed) # Shows that 'with open' is not closed.
    # # The connection is open and alive.
    # file_contents = file_obj.read()
    # print(file_contents) # Prints all the text from 'sample_text'

    # for line in file_obj: # Accesses each line one at a time.
    #     print(line) # Prints all text from 'sample_text,' but also spaces it out.

    """
### Lines ###
    file_content = file_obj.readline() # Reads one line.
    print(file_content) # With every other inside code cancelled, only the first line will display.

    file_content = file_obj.readline()
    print(file_content) # Second line.

    file_content = file_obj.readline()
    print(file_content) # Third line.
    
    """

    """
### Characters ###
    size_read = 100 # Reads 100 characters.

    file_contents = file_obj.read(size_read) # Connects 'size_read' and 'file_contents'
    print(file_contents) # Prints the first 100 characters.

    file_contents = file_obj.read(size_read)
    print(file_contents) # Next 100 characters.

    file_contents = file_obj.read(size_read)
    print(file_contents) # Next 100 characters.
    # No more characters means no more characters to print.
    """

    """
    size_read = 100
    file_contents = file_obj.read(size_read)
    while len(file_contents) > 0: # Cheap way to use 'while,' since the file is greater than 0.
        print(file_contents, end="*") # * is used to stop the loop.
        file_contents = file_obj.read(size_read) # Also used to stop the loop.

    """
# print(file_obj.closed) # Prints 'True' to show that it is closed.
# # Perfect for testing if a file is closed or not.










##### WRITE #####
# with open('write_test.txt', 'w') as file_obj: # 'w' represents write.
#     file_obj.write('Writing') # Makes a new file 'write_test' and writes 'Writing' in it.

# Combining read and write
# with open ('sample_text', 'r') as read_obj: # Read
#     with open('sample_text_copy', 'w') as write_obj: # Write
#         for line in read_obj:
#             write_obj.write(line) # makes new file 'sample_text_copy' and adds the lines from 'sample_text.'

##### OVERWRITING #####
with open ('sample_text', 'r') as read_obj:
    with open('sample_text_copy', 'a') as write_obj:
        # Using 'w' overwrites existing data.
        # Using 'a' (append) adds on new word 'Rewrite again'
        write_obj.write("\n" + 'Rewrite again and again') # Prints in 'sample_text_copy'
        # "\n" makes a new line and prints the text on it.


# csy, excel --> pandas









##### JSON INTRO #####
# JSON stands for Java Script Object Notation.

emp_data = '''
{
    "employees": [
        {
            "name": "John",
            "age": 29
            "emails": ["john@gmail.com", "john@outlook.com"]
        },
        {
            "name": "Jane",
            "age": 48
            "emails": null
        }
    ]
}
'''
# Heads up: the json file didn't work for me for some reason. Had SONDecodeError.
import json
# To load json string into a python object
json_data = json.loads(emp_data)
'''
print(json_data)
print(type(json_data))
print(json_data['employees'])

for emp in json_data['employees']:
    print(emp['name'])

# Delete the email for each employee and then load it into a json string.
for emp in json_data['employees']:
    del emp['emails']

print(json_data)

# Convert a python object into a json string
new_str = json.dumps(json_data, indent = 2) # Indents the lines.
print(new_str)
print(type(new_str))
'''

# Load json data from a file into python object
with open('states.json', 'r') as file_obj:
    data = json.load(file_obj)

# print(data)
# print(type(data))

for state in data['states']:
    print(state['name'], state['abbreviation'])

    # Remove the area code for each state
    del state['area_codes']

print(data['states'])

# To write json data to a file
with open('new_states.json', 'w') as file_obj:
    json.dump(data, file_obj, indent = 2)


# API --> Application Programming Interface
"""
Address --> user entered address , recommended address 16701-1234
web application --> USPS public API --> valid and return appropriate address
"""

"""
Fidelity Investments --> facebook page, twitter handle, linkedin page
Facebook API --> JSOm format
post, comments, replies etc.
"""

# import random
# random.random() # The first random is a package. The second random is a module.









##### REQUESTS INTRO #####
from urllib.request import urlopen
import json

with urlopen("https://dummyjson.com/users") as response:
    api_response = response.read()

# print(api_response) # prints the data from the api.

data = json.loads(api_response)
print(data)

print(json.dumps(data, indent=2)) # Gives proper format.

for user in data['users']:
    print((user['email'])) # Gives access to the email addresses.

with open('users_emails.txt', 'w') as emails_obj:
    for user in data['users']:
        emails_obj.write(user['email'] + "\n")
