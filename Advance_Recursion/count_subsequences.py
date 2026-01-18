"""
Count the all subsequences
"""
class Solution:
    def count_subsequences(self,nums,target):
        """
        Time Complexity : O(2**n)
        Space Complexity : O(n)
        """
        zeros=nums.count(0)
        nums=[x for x in nums if x!=0]
        def backtrack(index,total):
            if total==target:
                return 1
            if total>target or index>=len(nums):
                return 0
            
            sum=total+nums[index]
            pick=backtrack(index+1,sum)
            sum=total
            not_pick=backtrack(index+1,sum)
            return pick+not_pick
        return backtrack(0,0)*(2**zeros)

s=Solution()
nums=[0,9,0]
target=0
print(s.count_subsequences(nums,target))