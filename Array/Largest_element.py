"""
Find the largest element in the array
"""
nums=[55,32,-97,99,3,67]
largest=nums[0]
for i in range(1,len(nums)):
    if nums[i]>largest:
        largest=nums[i]

print(largest)