""" Sort by the second letter
Add a key parameter and a lambda function to return the second character """

#list
y = ["pig", "cow", "horse"]
print(sorted(y, key=lambda k:k[1]))

#tuple
z = ("kevin", "niklas", "jenny", "craig")
print(sorted(z, key=lambda k:k[1]))