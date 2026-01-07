"""
Remove duplicates from a sorted doubly linked list

Link : https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1

Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is 
retained, rest nodes with value = 1 are deleted.
"""
from Double_creation import Double_linked_link
class Solution(Double_linked_link):
    def remove_duplicates(self):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        curr=self.head
        while curr:
            if curr.prev and curr.prev.val==curr.val:
                if curr.prev==self.head:
                    curr.prev=None
                    self.head=curr
                else:
                    curr.prev.prev.next=curr
                    curr.prev=curr.prev.prev
            curr=curr.next
        return self.head
    
s=Solution()
s.append(1)
s.append(1)
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(4)
s.append(4)
s.traversal()
print()
s.remove_duplicates()
s.traversal()


