"""
find the maximum depth of binary tree means height
link : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 
"""
from implementation import Binary_Node
class Solution:
    def maximum_depth(self,node):
        if node is None:
            return 0
        lh=self.maximum_depth(node.left)
        rh=self.maximum_depth(node.right)
        return 1+max(lh,rh)


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
print(s.maximum_depth(three,0))
        


