"""
brute force approach to move all zeros to end of array
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
like input: [0,1,0,3,12]
output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self,nums):
        n=len(nums)
        temp=[]
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
        for i in range(0,len(temp)):
            nums[i]=temp[i]
        for i in range(len(temp),n):
            nums[i]=0
        print(nums)
s=Solution()
nums=[0,1,0,3,12]
s.moveZeroes(nums)
"""
time complexity: O(n)
space complexity: O(n)

"""

