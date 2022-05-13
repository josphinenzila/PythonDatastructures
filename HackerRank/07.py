""" Arrays """

#Given an array, A, of N integers, print A's elements in reverse order as a single
#line of space-separated numbers
n = int(input("Enter the value of n: ").strip())
arr = [int(arr_temp) for arr_temp in input("Enter the list of your array: ").strip().split(' ')]

reversed_array = []
for i in range(len(arr)):
    reversed_array.append(arr[n-i-1])

print(' '.join(str(i) for i in reversed_array))

