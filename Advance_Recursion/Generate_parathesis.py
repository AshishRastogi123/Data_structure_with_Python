"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Link : https://leetcode.com/problems/generate-parentheses/description/

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
class Solution:
    def solve(self,index,total,bracket,result):
        if index==len(bracket):
            if total==0:
                result.append("".join(bracket))
            return
        if total>len(bracket):
            return
        elif total<0:
            return
        bracket[index]="("
        sum=total+1
        self.solve(index+1,sum,bracket,result)
        bracket[index]=")"
        sum=total-1
        self.solve(index+1,sum,bracket,result)
        
        

    def generate_parathesis(self,n):
        """
        Time Complexity : O(2^n)
        Space Complexity : O(2*n)
        """
        brackets=[""]*n*2
        result=[]
        self.solve(0,0,brackets,result)
        return result
    
s=Solution()
print(s.generate_parathesis(3))