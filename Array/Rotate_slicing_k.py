"""
rotate using slicing
"""
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)

s=Solution()
nums=[5,-2,3,9,0,10,7]
k=10
s.rotate(nums,k)

"""
time complexity: O(n)
space complexity: O(1)
"""