"""
39. Combination Sum

Link : https://leetcode.com/problems/combination-sum/description/

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
class Solution:
    def solve_sum(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if index>=len(nums):
            return
        sum=total+nums[index]
        subset.append(nums[index])
        self.solve_sum(index,sum,subset,nums,target,result)
        sum=total
        subset.pop()
        self.solve_sum(index+1,sum,subset,nums,target,result)
        
        
            
    def combination_sum(self,candidate,target):
        """
        Time Complexity : O(2^t*k) where t is the how many number of times you pick an element
        Space Complexity : O(t)
        """
        result=[]
        self.solve_sum(0,0,[],candidate,target,result)
        return result
    
s=Solution()
candidates = [2,3,6,7]
target = 7
p=s.combination_sum(candidates,target)
print(p)