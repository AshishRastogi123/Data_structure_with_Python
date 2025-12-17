"""
53. Maximum Subarray

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
nums = [5,4,-1,7,8]
class Solution:
    def max_subarray_brute(self,nums):
        total=0
        maxi=float("-inf")
        for i in range(len(nums)):
            total=nums[i]
            for j in range(i+1,len(nums)):
                total+=nums[j]
                if total>maxi:
                    maxi=total
        print(maxi)
    def max_sub_optimal(self,nums):
        total=0
        maxi=float("-inf")
        for i in range(len(nums)):
            if total<0:
                total=0
            total+=nums[i]
            if total>maxi:
                maxi=total
        print(maxi)
        return maxi
s=Solution()
s.max_sub_optimal(nums)
