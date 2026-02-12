"""
Prefix To Postfix Conversion

link : https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1

Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*
Explanation: 
The above output is its valid postfix form.
"""
class Solution:
    def preToPost(self, pre_exp):
        stack=[]

        for i in range(len(pre_exp)-1,-1,-1):
            char=pre_exp[i]

            if char.isalnum():
                stack.append(char)
            else:
                operant1=stack.pop()
                operant2=stack.pop()

                new_exp=operant1+operant2+char
                stack.append(new_exp)

        return stack[-1]
s=Solution()
print(s.preToPost("*-A/BC-/AKL"))