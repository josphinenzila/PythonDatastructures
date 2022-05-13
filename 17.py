""" sets """

#constructors - creating new sets
x = {3, 5, 3, 5}
print(x)

y = set()
print(y)

list1 = [2, 3, 4]
z = set(list1)
print(z)

#set operations
x = {2, 3, 8, 5}
print(x)

#add
x.add(7)
print(x)

#remove
x.remove(3)
print(x)

#get length of set x
print(len(x))

#check membership in x
print(5 in x)

#pop random item from set x
print(x.pop(), x)

#delete all the items from set x
print(x.clear())

