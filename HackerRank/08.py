""" Dictionaries and Maps """

#Given n names and phone numbers, assemble a phonebook that maps friends names
#to their respective phone numbers. You will be given an unknown number to query and name to query your phone book for

import sys

n = int(sys.stdin.readline().strip())

phone_book = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split(" ")
    phone_book[entry[0]] = entry[1]
query = sys.stdin.readline().strip()
while query:
    phone_number = phone_book.get(query)
    if phone_number:
        print(query + "=" + phone_number )
    else:
        print("Not Found")
    query = sys.stdin.readline().strip()