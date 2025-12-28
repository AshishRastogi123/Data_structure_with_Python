"""
Docstring for Binary_search.py.Number_of_occurance

"""

class Solution:
    def number_of_occurance(self,nums,target):
        """
        Time Complexity : O(log(n))
        Space Complexity : O(1)
        """
        # if target not in nums:
        #     return [-1,-1]
        n=len(nums)
        if n==0:
            return 0
        low=0
        high=n-1
        lb=-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        if lb==-1 or nums[lb]!=target:
            return 0
        
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub-lb
    
    def brute_force(self,nums,target):
        """
        Time Complexity : O(log(n))
        Space Complexity : O(1)
        """
        if len(nums)==0:
            return 0
        first=-1
        last=-1
        for i in range(len(nums)):
            if nums[i]==target:
                if nums[i]==target:
                    if first==-1:
                        first=i
                    last=i
                elif nums[i]>target:
                    break
        if first==-1:
            return 0
        return last-first+1



s=Solution()
nums=[1,2,3,3,3,4,5,6,7,7,7,8,8,9,10,10,11,12,12]
target=3
p=s.number_of_occurance(nums,target)
print(p)
