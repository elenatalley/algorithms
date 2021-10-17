def F(n):
    if n < 11:
        print(n)
        F(n+4)
        F(n*2)
    else:
        print(f"cycle is over for {n}")

F(5)

"""
median
"""
num_list  = [2,6,5]
num_list.sort()
num_list[len(num_list) // 2]
print(num_list)
