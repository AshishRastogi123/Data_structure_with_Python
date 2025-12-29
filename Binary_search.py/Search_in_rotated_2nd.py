"""
81. Search in Rotated Sorted Array II

link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""
class solution:
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
                return True
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            
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
        return False

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
s=solution()

p=s.optimal(nums,target)
print(p)