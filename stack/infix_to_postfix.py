"""
Docstring for stack.infix_to_postfix

link : https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

Input: s = "a*(b+c)/d"
Output: abc+*d/
Explanation: The expression is a*(b+c)/d.
First, inside the brackets, b+c becomes bc+.
Now the expression looks like a*(bc+)/d. Next, multiply a with (bc+), so it becomes abc+* . 
Finally, divide this result by d, so it becomes abc+*d/.
"""
class Solution:
    def precidence(self,ch):
        if ch=='+' or ch=='-':
            return 1
        if ch=='*' or ch=='/':
            return 2
        if ch=='^':
            return 3
        return 0
        
    def infixtoPostfix(self,s):
        stack=[]
        result=[]
        count=0

        for char in s:
            if ("a"<=char<='z') or ('A'<=char<='Z') or ('0'<=char<='9'):
                result.append(char)
            elif char=='(':
                stack.append(char)

            elif char==')':
                while stack and stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precidence(stack[-1])>=self.precidence(char) and char!='^':
                    result.append(stack.pop())
                stack.append(char)
            
        while stack:
            result.append(stack.pop())
        return "".join(result)

y=Solution()
print(y.infixtoPostfix("a*(b+c)/d"))