"""
nums=[5,1,1,9,2,3,10]
target = 9
if subsequence exist return true otherwise false
"""
class Solution:
    def check_subsequence(self,nums,target):
        """
        Time Complexity : O(2**n)
        space Complexity : O(n)
        """
        result=[]
        def backtrack(index,total,subset):
            if total==target:
                result.append(subset.copy())
                return True
            elif total>target:
                return False
            if index>len(nums):
                return False
            subset.append(nums[index])
            sum=total+nums[index]
            pick=backtrack(index+1,sum,subset)
            if pick==True:
                return True
            subset.pop()
            sum=total
            not_pick=backtrack(index+1,sum,subset)
            return not_pick
        return backtrack(0,0,[])
    
    def optimal(self,nums,target):
        """
        Time Complexity : O(2**n)
        space Complexity : O(1)
        """
        def backtrack(index, total):
            if total == target:
                return True
            if total > target or index == len(nums):
                return False
        
            
            pick=backtrack(index + 1, total + nums[index])
            if pick:
                return True
            
            not_pick=backtrack(index + 1, total)
            return not_pick
    
        return backtrack(0, 0)
    

s=Solution()
nums=[5,1,9,3]
target=9
print(s.optimal(nums,target))