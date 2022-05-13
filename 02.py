""" Slicing involves slicing out substrings, sublists and subtuples using 
indexes[start:end+1:step] """

#The start is inclusive while the end is not
#When step is not defined, the default step is one
x = "computer"
print(x[1:4])

#Here step is 2
print(x[1:6:2])

#When the end is not defined then you pick upto the last character
print(x[3:]) 

#when start is not defined you start with the first character
print(x[:5])

#-1 always stands for the last character/index
print(x[-1])

#from the 3rd last index to the end
print(x[-3:])

#from start to the 2nd last
print(x[:-2])