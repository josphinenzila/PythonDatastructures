""" Mathematical set operations """

s1 = {1, 2, 3}
s2 = {3, 4, 5}

#Intersection(AND) - Finds the common items in the sets
print(s1 & s2)

#Union(OR) - Returns all the items in the sets
print(s1 | s2)

#Symmetrical Difference(XOR) - Returns items not common in the sets
print(s1 ^ s2)

#Difference(Subtraction)
print(s1 - s2)

#all elements in set s1 are contained in set s2(Subset)
print(s1 <= s2)

#all elements in set s2 are contained in set s1(superset)
print(s1 >= s2)