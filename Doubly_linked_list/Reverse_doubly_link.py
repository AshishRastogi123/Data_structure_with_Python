"""
Reverse a doubly linked list

link : https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
"""
from Double_creation import Double_linked_link
class Solution(Double_linked_link):
    def brute_force(self):
        """
       Time Complexity : O(n)
       Space Complexity : O(n)
        """
        temp=self.head
        stack=[]
        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp=self.head
        while temp:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return self.head
    
    def reverse(self):
        if self.head.next is None:
            return self.head
        curr=self.head
        prev=None
        
        while curr is not None:
            front=curr.next
            curr.next=prev
            curr.prev=front
            prev=curr
            curr=front
        self.head=prev
        return self.head


            

s=Solution()
s.append(45)
s.append(78)
s.append(89)
s.append(75)
s.append(34)
s.append(67)
s.traversal()
print()
s.reverse()
s.traversal()



