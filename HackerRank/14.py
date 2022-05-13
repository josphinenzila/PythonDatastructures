""" Scope """

#Complete the diffirence class by writing the following
#A class constructor that takes an array of integer as a parameter and saves it to the elements
# instance variable
#A complete diffirence method that finds the maximum absolute diference btn any 2 numbers in N 
# and stores it in the maximumDiffrerence instance variable

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        min_element = 101
        max_element = 0
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element

        self.maximumDifference = max_element - min_element


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
