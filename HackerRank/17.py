""" Throwing exceptions """

#Write a calculator class with a single method: int power(int, int). 
#The power method takes integers, n and p as parameters and returns the integer
# result of n**p. If either n or p is negative, then the method must throw an exception 
# with the message N and P should be non-negative

class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0 :
            raise Exception("n and p should be non-negative")
        else:
            return pow(n, p)


myCalculator=Calculator()
T=int(input("Enter the range: "))
for i in range(T):
    n,p = map(int, input("Enter the values of p and n: ").split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)