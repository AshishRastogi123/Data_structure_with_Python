"""
Diameter of Binary Tree
link : https://leetcode.com/problems/diameter-of-binary-tree/description/

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from implementation import Binary_Node
class Solution:
    diameter=0
    def solve(self,node):
        """
        Time Complexity : O(N)
        Space Complexity: O(H)
        """
        self.diameter_of_binary(node)
        return self.diameter
    

    def diameter_of_binary(self,node):
        if node==None:
            return 0
        lf=self.diameter_of_binary(node.left)
        rf=self.diameter_of_binary(node.right)
        self.diameter=max(self.diameter,lf+rf)
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
print(s.solve(one))
