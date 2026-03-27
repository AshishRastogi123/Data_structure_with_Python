"""
Top View of Binary Tree
You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note:

Return the nodes from the leftmost node to the rightmost node.
If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view. 
Link : https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

Input: root = [10, 20, 30, 40, 60, 90, 100]
Output: [40, 20, 10, 30, 100]
Explanation: The Green colored nodes represents the top view in the below Binary tree.
"""
from collections import deque
from implementation import Binary_Node
class Solution:
    def Top_view(self,root):
        """
        Time Complexity: O(N)+ O(nlogn) + O(n)=O(2n)=o(n)
        space complexity: O(n) + O(n)==O(2n)=O(n)
        """
        if root==None:
            return None
        ans=[]
        result={}
        queue=deque()
        queue.append((root,0))
        while queue:
            e,line=queue.popleft()
            if line not in result:
                result[line]=e.val
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))

        for values in sorted(result.items()):
            ans.append(values[1])
        return ans



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
print(s.Top_view(one))