##### FIND INDEX MODULE #####
# Write a function that returns the index of a given element.
# ['apples', 'oranges', 'kiwi', 'mango']

if __name__ == '__main__': # This condition makes sure that lines 6,7,8 would only run if this file run directly.
    print('Imported finding index module')
    test_var = 'Test String'
    print('Running find index module: ', __name__)
# __name__ = dunder variable



### 1 ###
def find_index(search_list, target_val): # Its taking both search_list & target_val.
    for idx, val in enumerate(search_list): # enumerate returns two values; index and the value.
        # print(idx, val)
        if val == target_val:
            return idx
    return 5

print(find_index(['apples', 'oranges', 'kiwi', 'mango'], 'mango'))
# Prints out the list and counts each value in order.


# Yeah, this is all messed up, but we have imported this file to modules_intro file.




