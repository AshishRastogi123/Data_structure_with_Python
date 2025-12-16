"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""
nums = [1,1,0,1,1,1]
def myself(nums):
    n=[]
    p=1
    for i in range(1,len(nums)):
        if nums[i-1]==nums[i]:
            p+=1
            n.append(p)
        else:
            p=1
    print(n)
    print(max(n))
def optimal(nums):
    count=0
    max_count=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            count+=1
        if count>max_count:
            max_count=count
        if nums[i]==0:       
            count=0
    print(max_count)
def best(nums):
    count=0
    max_count=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            count+=1
            if count>max_count:
                max_count=count
        else :       
            count=0
    print(max_count)
best(nums)
