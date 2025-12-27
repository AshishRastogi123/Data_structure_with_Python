"""
35. Search Insert Position
note-: here all element mare unique and sorted

link : https://leetcode.com/problems/search-insert-position/description/

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
"""
class Solution:
    def brute_force(self,nums,target):
        """
        Time Complexity : O(n)
        """
        for i in range(len(nums)):
            if target<=nums[i] and nums[i-1]<target:
                return i
            elif target<=nums[i] and i==0:
                return i
            
        return len(nums)
    
    def optimal(self,nums,target):
        """
        Time Complexity : O(log(n))
        Space Complexity : O(1)
        """
        n=len(nums)
        low=0
        high=n-1
        lb=n
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb




s=Solution()
nums = [1,3,5,6]
target = 4
p=s.brute_force(nums,target)
print(p)
o=s.optimal(nums,target)
print(o)
