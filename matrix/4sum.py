"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

link : https://leetcode.com/problems/4sum/description/

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
class Solution:
    def brute_force(self,nums,target):
        """
        Time Complexity : O(n^4)
        space complexity : O(n)
        """
        n=len(nums)
        if n<4:
            return []
        s=set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):

                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            temp=[nums[i],nums[j],nums[k],nums[l]]
                            temp.sort()
                            s.add(tuple(temp))
        return [list(i) for i in s]

    def better(self,nums,target):
        """
        Time Complexity : O(n^3)
        Space Complexity : O(N)
        """
        result=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                my_set=set()
                for k in range(j+1,n):
                    forth=target-(nums[i]+nums[j]+nums[k])    
                    if forth in my_set :
                        temp=[nums[i],nums[j],nums[k],forth]
                        temp.sort()
                        result.add(tuple(temp))
                    my_set.add(nums[k])
        return [list(i) for i in result]
    
    def optimal(self,nums,target):
        """
        Time Complexity: O(n^3)
        Space Complexity : O(number of list in result) which i used the ==O(1) think
        """
        result=[]
        nums.sort()
        n=len(nums)

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j> i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<1 :
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total==target :
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
                    elif total < target:
                        k+=1
                    else:
                        l-=1
        return result
                




s=Solution()
nums = [1,0,-1,0,-2,2]
target = 0
m=s.better(nums,target)
print(m)