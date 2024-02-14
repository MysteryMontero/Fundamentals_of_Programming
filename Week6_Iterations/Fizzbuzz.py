
# ### FIZZBUZZ
# # target num = 20
#      1
#      2
#     FIZZ -> divisible by 3
#      4
#     Buzz -> divisible by 5
#      6
#      7
#   FizzBuzz -> divisible by both 3 & 5

target_num = int(input('Enter a target: '))

for num in range(1, target_num+1):
    if num % 3 == 0 and num % 5 == 0: # Any numbers divided by 3 and 5 will have FizzBuzz in its place.
        print('FizzBuzz')
    elif num % 3 == 0: # Any number divided by 3 will have Fizz in its place.
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)