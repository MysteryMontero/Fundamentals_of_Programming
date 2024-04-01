##### MODULES #####
# Random, math, and reduce.

# 1. Standard, in-built: Already built in. EX: import random. Random, math, & reduce are all standard modules.

# 2. External modules: Not part of a language, will have to install before importing. EX: Pandas, Numpy.

# 3. Custom: Module that is built by developers for their specific thees.


# Standard module
# import random

# External module --> Needs to be installed first
# import pandas



### 2 ###
# import pandas
# import find_index_module as fim
# # Import pandas as pd, wherever possible, stick to conventions.
#
# req_idx = fim.find_index(['apples', 'oranges', 'kiwi', 'mango'], 'mango')
# print(req_idx)
# print(fim.test_var)



### 3 ###
# To import only specific things:
from find_index_module import find_index as fi
req_idx = fi(['apples', 'oranges', 'kiwi', 'mango'], 'mango')
print(req_idx)
# print(test_var)
print('Running modules intro: ', __name__)

# It transports from one file to the other.
