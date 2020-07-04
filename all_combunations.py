
'''
find all possible combinations for numbers in string
'''
import itertools

s = '1,2,3,4'
array = itertools.permutations([1,2,3,4])
for i in array:
    print(i)
