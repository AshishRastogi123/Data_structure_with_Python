"""
apply binary search
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Link : https://leetcode.com/problems/binary-search/description/
"""

class Solution:
    def binary_search(self, nums, target):
        """
        Docstring for binary_search
        :param self: Description
        :param nums: Description
        :param target: Description
        """
        n=len(nums)
        low=0
        high=n-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1

    def recursion_solution(self,nums,target):
        low=0
        high=len(nums)-1
        def binary_search(nums,target,low,high):        
            if low> high:
                return -1
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] <target:
                return binary_search(nums,target,mid+1,high)
            else:
                return binary_search(nums,target,low,mid-1)
        return binary_search(nums,target,low,high)
            

s=Solution()
nums = [-1,0,3,5,9,12]
target = 9
p=s.recursion_solution(nums,target)
print(p)

