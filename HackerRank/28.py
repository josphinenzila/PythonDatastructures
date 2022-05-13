""" Regex """

import math
import os
import random
import re
import sys

if __name__ == "__main__":
    N = int(input())
    pattern = r"@gmail\.com$"
    regex.re.compile(pattern)
    FirstNameList = []

    for N_itr in range (N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if regex.search(emailID):
            FirstNameList.append(firstName)
    FirstNameList.sort()
    for name in FirstNameList:
        print(name)