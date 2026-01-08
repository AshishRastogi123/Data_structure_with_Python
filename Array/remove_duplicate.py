"""
Remove duplicate from an sorted array

link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
class Solution:
    def bad_method(self,nums):
        """
        Time Complexity : 2O(n)
        Space Complexity : O(1)
        """
        nums[:]=list(set(nums))
        nums.sort()
        return nums
    
    def optimal(self,nums):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
                

s=Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
p=s.optimal(nums)
print(p)