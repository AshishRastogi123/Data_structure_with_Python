from implementation import Binary_Node
class Solution:
    def pre_order(self,node,):
        """
        Time Complexity : O(n)
        Space Complexity: O(h) where h is height of the tree and n is the number of nodes
        """
        if node==None:
            return 
        print(node.val,end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def In_order(self,node):
        """
        Time Complexity : O(n)
        Space Complexity : O(h)
        """
        if node==None:
            return
        self.In_order(node.left)
        print(node.val,end=" ")
        self.In_order(node.right)
    

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
s.In_order(one)


