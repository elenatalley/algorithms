"""
bubble sort
"""
mylist = [4,2,7,3]
#
# cnt = 7
# while cnt != 0:
#     cnt = 0
#     for i in range(len(mylist)-1):
#         if mylist[i] > mylist[i +1]:
#             mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
#             cnt += 1
# print(mylist)

#find length of the list
n = len(mylist)
#will count changes
cnt = 0
# this code will go through all list 1 time
# but we need n-1 (на 1 обход меньше чем элементов в листе)=>
for run in range(n-1):
    #- run => do not compare last elements
    for i in range(n-1-run):
        if mylist[i] > mylist[i + 1]:
            mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
            cnt += 1

print(*mylist)
print(cnt)












# cnt = 8
# while cnt != 0:
#     cnt = 0
#     for i in range(len(mylist) - 1):
#         if mylist[i] > mylist[i+1]:
#             mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
#             cnt+=1
#
#
# print(mylist)
# print(len(mylist))
