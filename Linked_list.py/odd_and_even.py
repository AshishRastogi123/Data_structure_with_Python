"""
328. Odd Even Linked List

Link : https://leetcode.com/problems/odd-even-linked-list/description/

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
"""
from node_creation import Singly_linked_list, Node
class Solution(Singly_linked_list):
    def brute_force(self):
        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        if not self.head or not self.head.next:
            return self.head
        temp=self.head
        l1=[]
        while temp is not None:
            l1.append(temp.val)
            if temp.next:
                temp=temp.next.next
            else:
                break
        temp=self.head.next
        while temp is not None:
            l1.append(temp.val)
            if temp.next:
                temp=temp.next.next
            else:
                break
        temp=self.head
        for i in range(len(l1)):
            temp.val=l1[i]
            temp=temp.next

        return self.head
    
    def optimal(self):
        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        if not self.head or not self.head.next:
            return self.head
        odd=self.head
        even=self.head.next
        even_head=even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next=even_head
        return self.head

    
s=Solution()
s.appends(12)
s.appends(54)
s.appends(77)
s.appends(97)
s.appends(76)
s.appends(33)
s.traversal()
print()
s.optimal()
s.traversal()