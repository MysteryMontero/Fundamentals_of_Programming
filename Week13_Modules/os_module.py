import os

# get current working directory
print(os.getcwd()) # cwd - current working directory.


# Change to a different directory
# os.chdir('C:\\Fundamentals_of_Programming')
# # print(os.getcwd())


# List all the files at the current location
print(os.listdir())


# mkdir- creates a single directory
# makedirs- used to create a hierarchy of directories

# os.mkdir('Test_Dir') # Makes a new folder

# os.makedirs('Test_Dir1\\sub1\\sub2') # Makes a folder with folders inside

# os.rmdir('Test_Dir') # Removes the single folder

# os.removedirs('Test_Dir1\\sub1\\sub2') # Removes the hierarchy folder

# Be very careful when deleting things!

