# Code for recursion

# Rows = len(x)+1
# Columns = len(y)+1
# A: Stone
# B: Longest
def find_lcs(x, y):
    len_x = len(x) # Rows
    len_y = len(y) # Columns
    lcs_array = []
    for i in range(len_x+1): # Extra Row
        zero_row = [0] * (len_y + 1) # That many rows
        lcs_array.append(zero_row)
    for row in range(1, len_x+1):
        for col in range(1, len_y+1):
            if x[row-1] == y[col-1]: # Starts at 0, that's why -1 is there.
                lcs_array[row][col] = 1 + lcs_array[row-1][col-1]
            else:
                lcs_array[row][col] = max(lcs_array[row-1][col], lcs_array[row][col-1])
    for row1 in lcs_array:
        print(row1) # Gives the table
    return lcs_array[row][col]

str1 = 'stone'
str2 = 'longest'
print(find_lcs(str1, str2)) # Gives the answer

