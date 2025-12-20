"""
128. Longest Consecutive Sequence
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
class Solution:
    def Brute_force(self,nums):
        """
        Time complexity: O(n*n)
        Space Complexity: O(1)
        """
        max_count=0
        n=len(nums)
        for i in range(n):
            num=nums[i]
            count=1
            while num+1 in nums:
                count+=1
                num=num+1
            if count>max_count:
                max_count=count
        return max_count
    

    def Longest_con_seq(self,nums):
        """
        Time Complexity: O(nlog(n))
        space complexity: O(n)
        """
        nums.sort()
        last_smaller=float("-inf")
        count=0
        longest=0
        n=len(nums)
        for i in range(n):
            num=nums[i]
            if num-1==last_smaller:
                count+=1
                last_smaller=num
            elif num!=last_smaller:
                count=1
                last_smaller=num
            if count>longest:
                longest=count
        return longest
    def optimal(self,nums):
        """
        time complexity : O(n)
        space complexity :O(n)

        """
        count=0
        longest=0
        my_set=set()
        n=len(nums)
        for i in range(n):
            my_set.add(nums[i])
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
        

s=Solution()
nums=[0,3,7,2,5,8,4,6,0,1]
l=s.optimal(nums)
print(l)


