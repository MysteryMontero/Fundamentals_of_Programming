'''
######## LISTS ########
# 1. Allow duplicate data
# 2. Order is maintained
# 3. Allows heterogeneous data
list1 = [10, 'test', False, 23.24]
print(list1)

### Length of the list
print(len(list1))
### Allows indexing and slicing
print(list1[2])
print(list1[1:4])
print(list1[-2])
### Can hold other lists too
list2 = [34, 54.76, 'Hi', ['Hello', 45, False]]
print(list2[3][1])

### Create an empty list
countries = []
### New elements can be added to a list using append, insert, or extend
countries.append('Canada')
countries.append('France')
countries.append('Germany')
countries.append('France')
print(countries)
# append always add elements at the end of the list

countries.insert(2, 'Mexico')
# insert can be used to add an eleent at a particular location
countries2 = ['USA', 'Thailand', 'Denmark']
countries.extend(countries2)
# extend changes the object internally, but doesn't return anything
print(countries)
# print(countries.append(countries2))
countries.append(countries2)
print(countries)
# ['Canada', 'France', 'Mexico', 'Germany', 'France', 'USA', 'Thailand', 'Denmark', ['USA', 'Thailand', 'Denmark']]

countries.pop()
print(countries)

## SORT function
countries.sort() ## Sort the countries in alphabetical order
print(countries)

countries.sort(reverse = True)
print(countries)

### membership test
print('USA' in countries) # True
print('Russia' in countries) # False

## List to string
countries_str = ', '.join(countries)
print(countries_str)
# USA-Thailand-Mexico-Germany-France-France-Denmark-Canada

print(type(countries))
print(type(countries_str))

## String List
countries3 = countries_str.split(', ')
print(countries3)


### TUPLES ###
# 1. Cannot be modified i.e. cannot update, add or remove an element
# element
tuple1 = (12, 234, 4255, 23) ## Useful for inches, cms
print(tuple1[2])
tuple1[3]

##### SETS #####
## 1. Do not allow duplicates
## 2. order is not guaranteed

countries = {'Russia', 'China', 'Japan', 'Sudan', 'Japan'}
print(countries)

### SET Operations
countries1 = {'Russia', 'China', 'Japan', 'Sudan', 'Ethiopia', 'Greece'}
print(countries.union(countries1)) # combines 'countries' and 'countries1' but gets rid of any duplicates and keeps only one.
print(countries.intersection(countries1))

print(countries.difference(countries1))
print(countries1.difference(countries))


##### DICTIONARIES - A collection of key value pairs #####
employee = {
    "id": 1233,
    "name": "John",
    "skills": ['Java', 'PHP', 'Python'],
    "address": {
        "city": "LA",
        "state": "CA",
        "zip-code": 12344
    }
}
print(employee['address']['state']) # Access CA from the address


employee_dict = [
    {
    "id": 1233,
    "name": "John",
    "skills": ['Java', 'PHP', 'Python'],
    "address": {
        "city": "LA",
        "state": "CA",
        "zip-code": 12344
    }
  },
    {
    "id": 3233,
    "name": "John",
    "skills": ['Java', 'SQL', 'Python'],
    "address": {
        "city": "LA",
        "state": "CA",
        "zip-code": 12344
    }
  }
]
print(employee_dict[1]['skills'][1]) # Prints out SQL by going into the second employee_dict[1],
# go into skills, and going to SQL[1]


##### CREATING EMPTY COLLECTIONS #####
list1 = [] # Create a list
tuple1 = () # Create a tuple
set1 = {} # Create a set
print(type(set1)) # Determine the type of variable. In this case; set
dict1 = {} # Creates a dictionary
set1 = set()
tuple1 = (10,)


### ACCESSING ELEMENTS FROM COLLECTIONS ###
list1 = [32, 34, 5, [45, 364, 23], [34, 7, 10, [34, 657, 11]], 11]
print(list1[4][3][1])
## tuples also support indexing and slicing

set1 ={314, 219, 134}
# set1[1] will error out because set is un ordered and no indices are aligned in the elements

## Convert a list or a tuple to a set
list2 = [21, 4, 10, 13, 78, 4, 21]
set2 = set(list2) # also pass a tuple
print(set2) # Gets rid of duplicate numbers
'''

tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])

list1 = [44, 12, 578, 21, 134, 67]
print(list1[3:6])

list1 = [5, 10, 15, 20, 75, 100, 50]
print(list1.index(20))
list[position] = 200


