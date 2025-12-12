"""
Find the largest element in the array
"""
nums=[55,32,-97,99,3,67]
largest=float("-inf")
s_largest=float("-inf")
for i in nums:
    if i>largest:
        largest=i
for j in nums:
    if i>s_largest and i!=largest:
        s_largest=i
print(s_largest,largest)