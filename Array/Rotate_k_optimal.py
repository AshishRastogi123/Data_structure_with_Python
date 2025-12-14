"""
some optimal solutions are:
"""
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        for _ in range(k):
            last =nums.pop()
            nums.insert(0,last)
        print(nums)
s=Solution()
nums=[5,-2,3,9,0,10,7]
k=10
s.rotate(nums,k)

"""
time complexity: O(n)
space complexity: O(1)

"""
