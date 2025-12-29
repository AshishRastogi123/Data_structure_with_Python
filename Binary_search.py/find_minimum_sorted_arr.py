"""
find minimum element in an array

link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

153. Find Minimum in Rotated Sorted Array
isme duplicate nhi honge
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""
class Solution:
    def brute_force(self,nums):
        """
        Time Complexity : O(n)
        space Complexity : O(1)
        """
        minimum=float("inf")
        for i in range(len(nums)):
            if minimum>nums[i]:
                minimum=nums[i]
        return minimum
    
    def find_minimum_arr(self,nums):
        """
        Time Complexity : O(log(n))
        Space Complexity : O(1) or O(n)
        """
        n=len(nums)
        low=0
        high=n-1
        mini=float("inf")
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(nums[mid],mini)
                high=mid-1
            else:
                mini=min(nums[mid],mini)
                low=mid+1
        return mini


s=Solution()
nums = [3,4,5,1,2]
p=s.find_minimum_arr(nums)
print(p)