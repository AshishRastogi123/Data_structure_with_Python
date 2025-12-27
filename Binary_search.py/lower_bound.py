"""
Lower Bound problem with Binary Search

find the largest occuracance index which less than the target mean Floor in a Sorted Array

gfg= https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1.

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 11
Output: 4
Explanation: Largest Number less than or equal to 11 is 10, whose indices are 3 and 4. The index of last occurrence is 4.


"""
class Solution:
    def lower_bound(self,nums,target):
        """
        Lower Bound = first index i such that nums[i] ≥ target
        
        :param self: Description
        :param nums: Description
        :param target: Description
        """
        n=len(nums)
        low=0
        high=n-1
        lb=-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    
    def upper_bound(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub
    
    """
    last occurance throgh the upper bound
    """
    def last_occ_up(self,arr,x):
        n=len(arr)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(high+low)//2
            if arr[mid]>x:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub-1
    """
    gfg solution
    """
    def findFloor(self, arr, x):
        # code here
        n=len(arr)
        low=0
        high=n-1
        ub=-1
        while low<=high:
            mid=(high+low)//2
            if arr[mid]<=x:
                ub=mid
                low=mid+1
                
            else:
                high=mid-1
                
        return ub


s=Solution()
nums= [1,2,2,2,3,3,5,6,7,7,7,9,12,13]
target = 7
p=s.lower_bound(nums,target)
u=s.upper_bound(nums,target)
print(f"Number of occurance of {target} in {nums} is {u-p}")

new1=s.findFloor(nums,target)

print(f"last occurrence of largest number which is less than and equal to {target} index is {new1} ")

ls=s.last_occ_up(nums,target)
print(f"last occurance of {target} is {ls}")

