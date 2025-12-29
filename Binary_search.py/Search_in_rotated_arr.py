"""
search in a rotated array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

link : https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1
"""
class Solution:
    def search_in_rotated(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        for i in range(n):
            if i!=n-1 and nums[i]>nums[i+1]:
                low=i+1
                break
        f=low-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        high=f
        low=0
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1
    def brute_force(self,nums,target):
        """
        Time Complexity : O(n)
        space Complexity : O(1)
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
    def optimal(self,nums,target):
        """
        Time Complexity : O(log(n))
        space complexity : O(1)
        """
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            
            if nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return -1


nums = [6,7,1,2,3,4,5]
target = 3

s=Solution()
p=s.search_in_rotated(nums,target)
print(p)
b=s.brute_force(nums,target)
print(b)
o=s.optimal(nums,target)
print(o)