"""
199. Binary Tree Right Side View

Link : https://leetcode.com/problems/binary-tree-right-side-view/description/

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]
"""
from implementation import Binary_Node
from collections import deque
class Solution:
    def brute_force_sol(self,root):
        """
        Time Complexity : O(N)
        Space Complexity : O(N) + O(N)
        """
        if root is None:
            return []
        queue=deque()
        ans=[]
        queue.append(root)
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()
                if i==level_size-1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)            
        return ans
    
    def optimal(self,root):
        """
        Time Complexity : O(N)
        SPace COmplexity: O(H)
        """
        ans=[]
        level=0
        return self.solve(root,level,ans)
    def solve(self,node,level,ans):
        if node is None:
            return []
        if len(ans)==level:
            ans.append(node.val)
        if node.right:
            self.solve(node.right, level+1, ans)
        if node.left:
            self.solve(node.left,level+1,ans)   
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
print(s.brute_force_sol(one))