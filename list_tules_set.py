
l = ["can", "modified", "jkj"]
t = ("cant", "modified", "add", "removed")
# set , set() = empty set
s = {"can't", "have", "duplicate", "no_order"}

print(t[0])

# subscribed notation doesn't work for set (no order)
#

l[2] = "add"

l.append("can_append")
l.remove("can")
s.add("can_add_item")

print(l)

# compare sets from long to short
a = {1,2,3,4,5,6}
b ={1,2,3,4}
c = a.difference(b)
print(c)

d = a.union(b)
print(d)

both = a.intersection(b)
print(both)