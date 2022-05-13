""" Tuples """

#constructors- creating new tuples
x = 2,
print(x, type(x))

list1 = [2, 4, 6]
x = tuple(list1)
print(x)

#tuples are immutable, but member objects may be mutable
x = (1, 2, 3)
#del(x[1]) - fails
#x[1] = 8 - fails
print(x)

y = ([1, 2], 3)
del(y[0][1])
print(y)


y = y + (4,)
print(y)