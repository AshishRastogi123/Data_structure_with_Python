"""
78. Power Set 
Link : https://leetcode.com/problems/subsets/description/

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Soluton:
    def power_set(self,nums):
        """
        Time Complexity : O(n*2^^n)
        Space Complexity : O(2^n * n)
        """
        n=len(nums)
        total_subset=1<<n
        result=[]
        for i in range(total_subset-1):
            lst=[]
            for j in range(n):
                if i&(1<<j)!=0:
                    lst.append(nums[j])
            result.append(lst)
        result.append(nums)

        return result
    
s=Soluton()
print(s.power_set([1,2,3]))