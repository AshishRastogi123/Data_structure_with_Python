"""
124. Binary Tree Maximum Path Sum

Link : https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""
from implementation import Binary_Node
class Solution:
    maxi=float("-inf")
    def maximum_path(self,node):
        self.solve(node)
        return self.maxi

    def solve(self,node):
        if node==None:
            return 0
        lf=self.solve(node.left)
        if lf<0:
            lf=0
        rf=self.solve(node.right)
        if rf<0:
            rf=0
        self.maxi=max(self.maxi,lf+node.val+ rf)
        return node.val + max(lf,rf)

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
print(s.maximum_path(one))




