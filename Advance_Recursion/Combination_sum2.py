"""
40. Combination Sum II:
but here Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Link : https://leetcode.com/problems/combination-sum-ii/description/

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]    
"""
class Solution:
    def brute_force(self,nums,target):
        """
        Time Complexity : O(2^n x klog(k))
        space Complexity : O(n)
        """
        result=set()
        self.solve(0,0,[],nums,target,result)
        return list(result)
    
    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.add(tuple(sorted(subset)))
            return
        elif total>target:
            return
        
        if index==len(nums):
            return
        subset.append(nums[index])
        sum=total+nums[index]
        self.solve(index+1,sum,subset,nums,target,result)
        subset.pop()
        sum=total
        self.solve(index+1,sum,subset,nums,target,result)

    """
    Optimal Solution
    """
    def combination_sum2(self,nums,target):
        """
       Time Complexity : O(2^n * n)
       Space Complexity : O(n)

        """
        result=[]
        nums.sort()
        self.backtrack(0,[],nums,target,result)
        return result

    def backtrack(self,index,subset,nums,target,result):
        if target==0:
            result.append(subset.copy())
            return
        elif target<0:
            return
        if index>=len(nums):
            return
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            if nums[i]>target:
                break
            subset.append(nums[i])
            self.backtrack(i+1,subset,nums,target-nums[i],result)
            subset.pop()
        



s=Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
p=s.combination_sum2(candidates,target)
print(p)