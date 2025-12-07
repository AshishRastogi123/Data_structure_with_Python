"""
Print the Numbers from 1 to N using recursion
"""
def number(i,n):
    if i>n:
        return
    number(i,n-1)  
    print(n)    
number(1,50)
