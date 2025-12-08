def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

"""Factorial of Num whre from 1 to n
time complexity O(n)
space complexity O(n)
stack space O(n)
"""