"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

1. Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution:
    def brute_force(self,nums,target):
        """
        time complexity: o(n**2)
        space complexity: o(1)
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
    def some_optimal(self,nums,target):
            """
            Docstring for optimal
            
            :param self: Description
            :param nums: Description
            :param target: Description
            """
            for i in range(0,len(nums)):
                if abs(target-nums[i]) in nums:
                    return [i,nums.index(abs(target-nums))]
    def best(self,nums,target):
         hash_map={}
         for i in range(0,len(nums)):
              remainder=target-nums[i]
              if remainder in hash_map:
                   return [hash_map[remainder],i]
              hash_map[nums[i]]=i

              
         

s=Solution()
nums= [2,7,11,15]
target = 17
n=s.best(nums,target)
print(n)