"""
2220. Minimum Bit Flips to Convert Number
Link : https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

Example 1:

Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3
"""
class Solution:
    def convert_need_flip(self,start,goal):
        """
        Time Complexity : O(32)
        Space Complexity : O(1)
        """

        ans=start^goal
        count=0
        for i in range(32):
            if ans&(1<<i)!=0:
                count+=1
        return count
        

s=Solution()
print(s.convert_need_flip(3,4))