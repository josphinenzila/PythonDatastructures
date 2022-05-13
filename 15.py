""" Lists """

#list comprehension
a = [m for m in range(8)]
print(a)

b = [i**2 for i in range(10) if i>4]
print(b)

#delete a list or an item in a list
x = [5, 3, 8, 6]
del(x[1])
print(x)

#append an item to a list- to the end of the list- one item at a time
x = [5, 3, 8, 6]
x.append(7)
print(x)

#extend a sequence to a list - multiple items
x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y)
print(x)

#insert an item at a given index
x = [5, 3, 8, 6]
x.insert(1,7)
print(x)

x.insert(1, ["a", "m"])
print(x)

#pop last item off list and returns item
x = [5, 3, 8, 6]
x.pop()
print(x)

#remove the 1st occurence of an item
x = [5, 3, 8, 6, 3]
x.remove(3)
print(x)

#reverse - reverse the order of the list -  
#it is an in-place sort,meaning it changes the original list
x = [5, 3, 8, 6]
x.reverse()
print(x)

#sort - sort the list in place
#sorted(x) returns a new sorted list without changing the original list
#x.sort() puts the items of x in sorted order(sorts in place)
x = [5, 3, 8, 6]
x.sort()
print(x)

#reverse- sort - sorts items descending
x = [5, 3,8, 6]
x.sort(reverse=True)
print(x)

