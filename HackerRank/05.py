""" Loops """

#Given an integer n, print its first 10 multiples. Each multiple n*i should be printed on a new line in the form n*i = result

import sys

n = int(input("Enter your interger: ").strip())
for i in range(1, 11):
    product = n * i
    print("{} * {} = {}".format(n, i, product))
