"""
find maximum of two number
"""
def max(a,b):
    return (a+b+abs(a-b))/2

"""
if have an array then first sort it and return last element
"""
def max_array(c):
    return sorted(c)[-1]
p=max(88,100)
print(max_array([1,8,3,5]))
print(p)