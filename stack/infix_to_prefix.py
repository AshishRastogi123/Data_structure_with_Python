"""
Docstring for stack.infix_to_prefix

Link : https://www.geeksforgeeks.org/problems/infix-to-prefix-notation/1

Ex:
Input: s = "a*(b+c)/d"
Output: /*a+bcd
Explaination: The infix expression is a*(b+c)/d. First,
 inside the brackets, b + c becomes +bc. Now the expression looks like a*(+bc)/d. Next,
 multiply a with (+bc), so it becomes *a+bc. Finally, divide this result by d, so it becomes /*a+bcd.
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

    def infixToPrefix(self,s):
        s=s[::-1]
        s=s.replace('(','temp').replace(')','(').replace('temp',')')

        stack=[]
        result=[]

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
                while stack and (
                    self.precidence(stack[-1]) > self.precidence(char) or
                    (self.precidence(stack[-1]) == self.precidence(char) and char == '^')
                ):
                    result.append(stack.pop())
                stack.append(char)
            
        while stack:
            result.append(stack.pop())
        return "".join(result[::-1])
    
p=Solution()
print(p.infixToPrefix('h^m^q^(7-4)'))