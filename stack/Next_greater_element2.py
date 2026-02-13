"""
503. Next Greater Element II

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
"""
class Next_greater2:
    def optimal(self,nums):
        """
        Time Complexity : O(4N)
        Space Complexity : O(N)
        """
        n=len(nums)
        ans=[-1]*n
        stack=[]

        for i in range(2*n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n and len(stack)!=0:
                    ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans
    
s=Next_greater2()
nums = [1,2,1]
print(s.optimal(nums))