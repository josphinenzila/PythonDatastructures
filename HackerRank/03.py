""" conditional statements """

#if n is odd, print weird
#if n is even and in the inclusive range 2 and 5 print "Not weird"
#if n is even and the inclusive range of 6 to 20, print weird
#if n is even and greater than 20, print "Not weird"

import sys
N = int(input("Input your interger: ").strip())
if N % 2 == 1:
    print("Weird")
elif N < 5:
    print("Not Weird")
elif N <= 20:
    print("Weird")
else:
    print("Not weird")