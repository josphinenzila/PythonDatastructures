""" Interfaces """

#Complete the implementation of calculator class which implements the 
#advanced Arithmetic interface. The implementation for the divisorSum(n) 
#method must return the sum of all divisors

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self,n):
        divisor_sum = 0
        for i in range(1, n+1):
            if n%i == 0:
                divisor_sum += i
        return divisor_sum


n = int(input("Enter the value of n: "))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)