""" Exceptions """

#Read a string, s, and print it's integer value: if s cannot be converted to
# an integer, print bad string

S = input("Enter the string: ").strip()

try:
    integer_value = int(S)
    print(integer_value)
except ValueError:
    print('Bad String')