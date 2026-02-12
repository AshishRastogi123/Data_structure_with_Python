"""
PostFix to Infix conversion

link : https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1

Input:
ab*c+ 
Output: 
((a*b)+c)
Explanation: 
The above output is its valid infix form.
"""
class Solution:
    def Postfix_to_infix(self,postfix):
        """
        Time Complexity : O(N)
        Space Complexity : O(N)
        """
        stack=[]

        for char in postfix:
            if char.isalnum():
                stack.append(char)
            else:
                operant1=stack.pop()
                operant2=stack.pop()

                new_expre=f"({operant2}{char}{operant1})"

                stack.append(new_expre)

        return stack[-1]
    

s=Solution()
print(s.Postfix_to_infix("ab*c+"))
