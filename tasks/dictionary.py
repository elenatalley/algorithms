import operator

"""
Отсортируйте словарь по значению в порядке возрастания и убывания

"""
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Сортируем в порядке возрастания:
increase = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(increase)

# в порядке убывания
decrease = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(decrease)
"""
operator is a built-in module providing a set of convenient operators. 
In two words operator.itemgetter(n) constructs a callable that assumes 
an iterable object (e.g. list, tuple, set) as input, and fetches the 
n-th element out of it.
a.sort(key=lambda elem: elem[1])
Or just an ordinary function:

def get_second_elem(iterable):
    return iterable[1]

a.sort(key=get_second_elem)
https://www.rupython.com/operator-itemgetter-sort-python-61228.html
"""