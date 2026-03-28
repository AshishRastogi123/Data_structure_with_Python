"""
Bottom View of Binary Tree
link: https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
    
Output: [5, 10, 4, 28, 25]
Explanation: The Green nodes represent the bottom view of below binary tree.
"""
from implementation import Binary_Node
from collections import deque
class Solution:
    def Bottom_view(self,root):
        """
        Time Complexity: O(N)+ O(nlogn) + O(n)=O(2n)=o(n)
        space complexity: O(n) + O(n)==O(2n)=O(n)
        """

        if root is None:
            return None
        queue=deque()
        result={}
        ans=[]
        queue.append((root,0))
        while queue:
            e,line=queue.popleft()
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
print(s.Bottom_view(one))
            