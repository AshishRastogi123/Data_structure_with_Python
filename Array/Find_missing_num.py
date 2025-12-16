"""
Optimal solution
"""
nums=[0,1,2,4,5]
n=len(nums)+1
l=n*(n-1)/2
n=0
for i in range(len(nums)):
    n+=nums[i]
l=l-n
print(int(l))