"""
You're given a sorted array 'a' of 'n' integers and an integer 'x'.
Find the floor and ceiling of 'x' in 'a[0..n-1]'.

Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.

Link : https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401
Example:
Input: 
n=6, x=5, a=[3, 4, 7, 8, 8, 10]   

Output:
4

Explanation:
The floor and ceiling of 'x' = 5 are 4 and 7, respectively.
"""
class Solution:
    def ceil_the_floor(self,nums,target):
        floor=-1
        ceil=-1
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                return [nums[mid],nums[mid]]
            elif nums[mid]>target:
                ceil=nums[mid]
                high=mid-1
            else:
                floor=nums[mid]
                low=mid+1
        return[floor,ceil]

s=Solution()
x=5
a=[3, 4, 7, 8, 8, 10]   
print(s.ceil_the_floor(a,x))