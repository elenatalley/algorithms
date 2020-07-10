# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
#
# # OR
# print([i for i in a if i < 5])

d = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""return similar elements"""
# a=[]
# for elem in d:
#     if elem in b:
#         a.append(elem)

# OR

# a = set(b) & set(b)
# print(a)
"""
sirt dictionary incrising and dicreasing"""
dict_1 = {'s':1, 's':9, 'd':7}
# dict_2 = {B:8, S:9, H:77}
print(sorted(dict_1, reverse=True))