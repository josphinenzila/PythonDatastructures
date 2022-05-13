""" Recursion """

#write a factorial function that takes a positive interger N as a parameter and prints the result on N

import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input("Enter an interger: ").strip())
    result = factorial(n)
    print(result)