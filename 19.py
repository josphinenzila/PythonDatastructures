""" Dictionaries """

#Different ways of creating dictionaries
x = {"pork":25.3, "beef":33.8, "chicken":22.7}
x = dict([("pork",25.3), ("beef",33.8), ("chicken",22.7)])
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)

""" Dictionary operations """

#Add / Update
x["shrimp"] = 38.2
print(x)

#delete an item
del(x["shrimp"])
print(x)

#get the length of a dictionary
print(len(x))

#delete all items from dictionary
x.clear()
print(x)

#delete dictionary
del(x)
#print(x)

#Accessing keys and values in a dictionary
y = {"pork":25.3, "beef":33.8, "chicken":22.7}
print(y.keys())
print(y.values())
print(y.items())

#check membership in keys only
print("beef" in y)

#check membership in values only
print("clams" in y.values())

#iterating a dictionary
for key in y:
    print(key, y[key])

for k, v in y.items():
    print(k, v)
