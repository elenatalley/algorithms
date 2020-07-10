from heapq import nlargest
"""
merge 2 dictionaries /udate
"""
dict1 = {'a':2, 'b':8}
dict2 = {'Y':26, 'M':99}
merged_dict = {}
for i in (dict1, dict2):
    merged_dict.update(i)

    print(merged_dict)

"""
Найдите три ключа с самыми
высокими значениями в словаре 
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}."""

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = nlargest(3,my_dict, key=my_dict.get)
print(result)
