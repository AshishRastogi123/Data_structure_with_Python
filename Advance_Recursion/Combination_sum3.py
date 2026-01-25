"""
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

link : https://leetcode.com/problems/combination-sum-iii/description/

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
"""
class Solution:
    def combo_sum(self,k,n):
        """
        Time Complexity : O(2^m) where m=9
        Space Complexity : O(k)
        """
        result=[]
        self.solve(1,0,[],k,n,result)
        return result

    def solve(self,last,total,subset,k,n,result):
        if total==n and len(subset)==k:
            result.append(subset.copy())
        if total>n or len(subset)>k:
            return

        for i in range(last,10):
            sum=total+i
            subset.append(i)
            self.solve(i+1,sum,subset,k,n,result)
            subset.pop()
        


s=Solution()
k=3
n=9
print(s.combo_sum(k,n))