"""
move zeros to end of array
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
like input: [0,1,0,3,12]
output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self,nums):
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
        print(nums)

s=Solution()
nums=[0,1,0,3,12]
s.moveZeroes(nums)