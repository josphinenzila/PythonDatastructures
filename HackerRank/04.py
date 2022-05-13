""" class vs instance """

#class person with an instance age
#A constructor with parameter initial Age
#Assign initial age to age. If initial age is negative set age to zero and print Age not valid, setting age to 0
#Write the following instance classes
# 1. yearPasses() should increase age instance by 1
# 2. amIOld should perform the following conditional actions:
# --if age < 13 print, you are young
# --if age >= 13, and age < 18, print "You are a teenager"
# --otherwise print "You are old"

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
t = int(input("Enter number of prompts: "))
for i in range(0, t):
    age = int(input("Enter your age: "))
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
