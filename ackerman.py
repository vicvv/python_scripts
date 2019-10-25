'''
Problem 282 - Project Euler https://projecteuler.net/problem=282
For non-negative integers m, n, the Ackermann function A(m, n) is 
defined as follows:

See URL for the formula https://en.wikipedia.org/wiki/Ackermann_function

Find A(1, 0) = 2, A(2, 2) = 7 and A(3, 4) = 125.

'''
def ackerman(m,n):
    if(m == 0):
        return n+1
    elif m > 0 and n == 0:
        return ackerman(m-1,1)
    elif m > 0 and n>0:
        return ackerman(m-1,ackerman(m,n-1))

print(ackerman(1,0))
print(ackerman(2,2))
print(ackerman(3,4))
