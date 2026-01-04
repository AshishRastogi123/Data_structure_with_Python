"""
Docstring for Reverse_integer
link: https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def Reverse_integer(self,x):
        n=abs(x)
        p=0
        while n>0:
            k=n%10
            p=p*10+k
            n=n//10
        if p>2**31-1 or p<-(2**31-1):
            return 0
        if x<0:
            return -p
        return p

x=-2134
s=Solution()
print(s.Reverse_integer(x))