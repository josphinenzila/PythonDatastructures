""" Given a string, s, of length N is indexed from 0 to N-1
print it's even-indexed and odd-indexed characters as 
2 space separated strings on a single line """

num_text_cases = int(input("Enter your test cases: "))
for i in range(num_text_cases):
    test_string = input("Enter the string: ")
    even_indexed_characters = ""
    odd_indexed_characters = ""
    for j in range(len(test_string)):
        if j % 2 == 0:
            even_indexed_characters += test_string[j]
        else:
            odd_indexed_characters += test_string[j]
    print("{} {}".format(even_indexed_characters, odd_indexed_characters))