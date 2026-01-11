class Solution:
    def swap_using_bit(self,a,b):
        a=a^b
        b=a^b
        a=a^b
        return a,b
    
s=Solution()
a=10
b=7
print(f"before swap: a={a},b={b}")
p=s.swap_using_bit(a,b)
print(p)