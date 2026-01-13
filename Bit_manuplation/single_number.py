"""
136. Single Number

Link: https://leetcode.com/problems/single-number/description/

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
"""
class Solution:
    def brute_force(self,nums):
        """
        Time Complexity : O(n)+O(n/2+1)
        space complexity : O(n/2+1)
        """

        hash_map={}
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1

        for key in hash_map:
            if hash_map[key]==1:
                return key
    
    def optimal(self,nums):
        """
        Time Complexity : O(n)
        space complexity : O(1)
        """
        ans=0
        for i in nums:
            ans=ans^i
        return ans
            
            
    

s=Solution()
nums=[5,1,1,4,5,6,7,6,7]
p=s.brute_force(nums)
print(p)