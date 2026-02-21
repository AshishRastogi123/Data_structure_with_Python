"""
1423. Maximum Points You Can Obtain from Cards

Link : https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, 
choosing the rightmost card first will maximize your total score.
The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
"""
class Solution:
    def max_point_optimal(self,cardPoints,k):
        """
        Time Complexity : worst case O(2n) otherwise O(n)
        Space Complexity : O(1s)
        """
        maxi=left_sum=right_sum=0
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        for i in range(0,k):
            left_sum+=cardPoints[i]
        maxi=left_sum
        right_idx=n-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_idx]
            maxi=max(maxi,left_sum+right_sum)
            right_idx-=1
        return maxi





s=Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(s.max_point_optimal(cardPoints,k))