"""
Postfix to prefix conversion

link : https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1

Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.
"""
class Solution:
    def postToPre(self, post_exp):
        """
        Time Complexity : O(N)
        Space Complexity : O(N)
        """
        stack=[]

        for char in post_exp:
            if char.isalnum():
                stack.append(char)
            else:
                operant1=stack.pop()
                operant2=stack.pop()

                new_ex=f"{char}{operant2}{operant1}"
                stack.append(new_ex)
        return stack[-1]
    

s=Solution()
print(s.postToPre("ABC/-AK/L-*"))
