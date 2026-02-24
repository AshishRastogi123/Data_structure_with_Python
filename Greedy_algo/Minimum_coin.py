"""
Minimum number of Coins

Link : https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10 } and a target value n.

Input: n = 39
Output: 6
Explaination: 39 can be formed using 3 coins of 10 rupees, 1 coin of 5 rupees and 2 coins of 2 rupees so minimum coins required are 6.

Constraints:
1 ≤ n ≤ 106

"""
class Solution:
    def find_min_coin(self,n):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        currrency=[1, 2, 5, 10]
        count=0
        right=len(currrency)-1
        while n>0 and right>=0:
            if currrency[right]<=n:
                count+=1
                n-=currrency[right]
            else:
                right-=1
            
        return count
    
s=Solution()
print(s.find_min_coin(39))