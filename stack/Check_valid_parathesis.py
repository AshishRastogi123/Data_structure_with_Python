"""
Check valid parathesis

link : https://leetcode.com/problems/valid-parentheses/description/

20 question 

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false
"""
class Solution:
    def check_valid(self,s):
        """
        Time Coplexity : O(n^2)
        Space Complexity : O(n)
        """
        if len(s)%2!=0:
            return False
        stack=[]
        open_bracket=['[','{','(']
        close_bracket=[']','}',')']
        
        for i in range(len(s)):
            if s[i] in open_bracket:
                stack.append(s[i])
                continue
            if len(stack)==0:
                return False
            e=stack.pop()
            index1=open_bracket.index(e)
            index2=close_bracket.index(s[i])
            if index1!=index2:
                return False
        if len(stack)!=0:
            return False
        return True
    def Sir_solution(self,s):
        """
        Time Coplexity : O(n)
        Space Complexity : O(n)
        """
        stack=[]
        for bracket in s:
            if bracket=='{' or bracket=='[' or bracket=='(':
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                ch=stack.pop()
                if (bracket==')' and ch=='(') or (bracket==']' and ch=='[') or (bracket=='}' and ch=='{'):
                    continue
                else:
                    return False
        return len(stack)==0
    
    def most_optimal(self,s):
        """
        Time Coplexity : O(n)
        Space Complexity : O(n)
        """

        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != mapping.get(ch):
                    return False
        return not stack


s=Solution()
p="()[){}"
print(s.check_valid(p))
print(s.Sir_solution(p))