
def binary_search(list, item):
    # low and high = boarders of list where we are searching
    low = 0
    high = len(list) - 1


    # until this part  will have only 1 element we will check middle element:
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid
        # if number is more then we need
        if guess > item:
            high = mid - 1
        #  if number is less then we need
        else:
            low = mid + 1
    return None


my_list = [1,3,4,5,7,8,9,15]

print(binary_search(my_list, 8))
print(binary_search(my_list, 88))
print(binary_search(my_list, 1))