"""
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

Выведите все элементы, которые меньше 5
"""
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i+1 < 5:
#         print(i)
# # OR

print([elem for elem in a if elem < 5])

"""
Нужно вернуть список, который состоит
из элементов, общих для этих двух списков
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# for elem in a:
#     if elem in b:
#         c.append(elem)
#         print(c)

        # OR:
"""
Because sets cannot have multiple occurrences of the same element, it makes 
sets highly useful to efficiently remove duplicate values 
from a list or tuple and to perform common math operations like unions
and intersections
"""
# c = list(set(a) & set(b))
print(list(set(a) & set(b)))