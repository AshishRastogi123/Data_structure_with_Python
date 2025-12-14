"""
Rotate an array to the right by k places. lletcode


    """
class Solution:
    def rotate(self,nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k>0:
            n =nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i]=nums[i-1]
            nums[0]=n
            k=k-1
            self.rotate(nums,k)
        else:
            print(nums)
            return nums
    
s=Solution()
nums=[5,-2,3,9,0,10,7]
k=10 
s.rotate(nums,k)
"""
But it is not efficient as it uses recursion and has high time cosmplexity.
time complexity: O(n*k)
space complexity: O(k) due to recursion stack
"""
    

        
      