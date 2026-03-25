"""
110. Balanced Binary Tree

Link : https://leetcode.com/problems/balanced-binary-tree/description/

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 
"""
from implementation import Binary_Node
class Solution:
    yes=True
    def banlanced_binary(self,node):
        self.solve(node)
        return self.yes
    def solve(self,node):
        if node==None:
            return 0
        lf=self.solve(node.left)
        rf=self.solve(node.right)
        if abs(lf-rf)>1:
            self.yes=False
        return 1+max(lf,rf)
    
one=Binary_Node(1)
two=Binary_Node(2)
three=Binary_Node(3)
four=Binary_Node(4)
five=Binary_Node(5)
six=Binary_Node(6)
seven=Binary_Node(7)
eight=Binary_Node(8)
nine=Binary_Node(9)
ten=Binary_Node(10)

one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
four.left=eight
four.right=nine
five.right=ten

s=Solution()
print(s.banlanced_binary(one))

