"""
Remove all ocuurance of val present in list return len of elemnet without val any occurance

link : https://leetcode.com/problems/remove-element/description/

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
class Solution:
    def brute_force(self,nums,val):
        """
        Time Complexity : O(n) or O(n*n)
        space complexity : O(1)
        """
        k=0
        while k<len(nums):
            if nums[k]==val:
                nums.pop(k)
            else:
                k+=1
        return len(nums)
    
    def batter(self,nums,val):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        k=0
        while k<len(nums):
            if nums[k]==val:
                nums[k],nums[-1]=nums[-1],nums[k]
                nums.pop()
            else:
                k+=1
        return k
    
    def optimal(self,nums,val):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
    

s=Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
p=s.optimal(nums,val)
print(nums[:p])
