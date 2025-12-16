"""
move all zeros to the end of array
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
like input: [0,1,0,3,12]
output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self,nums):
        n=len(nums)
        if n==0:
            return
        i=0
        while i<n:
            if nums[i]==0:
                break
            i+=1
        if i==n:
            return
        for j in range(i+1,n):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        print(nums)
s=Solution()
nums=[0,1,0,3,12]
s.moveZeroes(nums)

"""
time complexity: O(n)
space complexity: O(1)
"""
