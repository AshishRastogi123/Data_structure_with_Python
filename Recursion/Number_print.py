"""
Print the Numbers from 1 to N using recursion
"""

def number(i,n):
    if i>n:
        return
    print(i)
    number(i+1,n)
number(1,50)