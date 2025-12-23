"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
link = https://leetcode.com/problems/3sum/

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
class Solution:
    def brute_force(self,nums):
        """
        Time Complexity : O(n*n*n)
        Space Coplexity : O(n)
        """
        r=set()
        for i in range(len(nums)):  
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):        
                    if nums[i]+nums[j]+nums[k]==0 :
                            temp=[nums[i],nums[j],nums[k]]
                            temp.sort()
                            r.add(tuple(temp))
        return [list(i) for i in r]
    
    def better(self, nums):
        """
        Time Complexity : O(n*n)
        Space Complexity : O(N)
        """
        result=set()
        for i in range(len(nums)):
                my_set=set()
                for j in range(i+1,len(nums)):
                    third=-(nums[i]+nums[j])
                    if third in my_set:
                        temp=[nums[i],nums[j],third]
                        temp.sort()
                        result.add(tuple(temp))
                    my_set.add(nums[j])
        return [list(i) for i in result]
    
    def optimal(self,nums):
        """
        Time complexity : O(n*n) +O(n*log(n))=O(n*n)
        Space Complexity : O(number of triplets we add) ==O(1) because we used only return variable
        """
        result=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                 continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                      j+=1
                elif total_sum>0:
                     k-=1
                else:
                     temp=[nums[i],nums[j],nums[k]]
                     result.append(temp)
                     j+=1
                     k-=1
                     #skip duplicates
                     while j<k and nums[j]==nums[j-1]:
                          j+=1
                     while j<k and nums[k]==nums[k+1]:
                          k-=1
        return result
   
s=Solution()
nums = [-1,0,1,2,-1,-4]
b=s.optimal(nums)
print(b)
