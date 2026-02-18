"""
1004. max-consecutive-ones-iii

link : https://leetcode.com/problems/max-consecutive-ones-iii/description/

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
class Solution:

    def brute_force(self,nums,k):
        """
        Time Complexity : O(n(n+1))==O(n^2)
        Space Complexity : O(1)

        Got TLE error
        """
        maxi=0
        for i in range(len(nums)):
            zero_count=0
            one_count=0
            for j in range(i,len(nums)):
                if zero_count>=k:
                    break
                if nums[j]==0:
                    zero_count+=1
                one_count+=1

            if maxi<one_count:
                maxi=one_count

        return maxi
                

    def better(self,nums,k):
        """
        Time Complexity : O(2n)
        Space Complexity : O(1)

        """
        left=right=zeros=maxi=0
        n=len(nums)
        while right<n:
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
    
    def optimal(self,nums,k):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)

        """
        left=right=zeros=maxi=0
        n=len(nums)
        while right<n:
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi

m=Solution()
nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(m.optimal(nums,k))