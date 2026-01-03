"""
Remove nth node from the the linked list from last
link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
from node_creation import Singly_linked_list
class Solution(Singly_linked_list):
    def brute_force(self,pos):
        """
        time complexity : O(n)
        space COmplexity : O(1)
        """
        count=0
        curr=self.head
        prev=None
        while curr is not None:
            count+=1
            curr=curr.next
        if pos==count:  # if need to remove head 
            return self.head.next
        pos=count-pos
        curr=self.head
        for _ in range(pos):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        del curr
        return self.head
    

    def optimal(self,pos):
        """
        Time Complexity : O(n)
        Space Complexitty : O(1)
        """
        s=self.head
        f=self.head
        for _ in range(pos):
            f=f.next
        if f==None:
            return self.head.next
        while f.next is not None:
            s=s.next
            f=f.next
        s.next=s.next.next
        return self.head

    
s=Solution()
s.appends(90)
s.appends(67)
s.appends(54)
s.appends(34)
s.appends(55)
s.traversal()
print()
s.optimal(2)
s.traversal()
            






