"""
Prefix to infix conversion

link : https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
"""
class Solution:
    def preToInfix(self, pre_exp):
        """
        Time Complexity : O(2N)
        Space Compelxity : O(N)
        """
        stack=[]
        for char in pre_exp[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operant1=stack.pop()
                operant2=stack.pop()

                new_ex=f"({operant1}{char}{operant2})"
                stack.append(new_ex)

        return stack[-1]
    
s=Solution()
print(s.preToInfix("*-A/BC-/AKL"))