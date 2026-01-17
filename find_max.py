"""
find maximum of two number
"""
def max(a,b):
    return (a+b+abs(a-b))/2

p=max(88,100)
print(p)