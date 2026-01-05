"""
Delete all the occurance of a target

link : https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1

Input: 
2<->2<->10<->8<->4<->2<->5<->2
2
Output: 
10<->8<->4<->5
Explanation: 
All Occurences of 2 have been deleted.

"""
from Double_creation import Double_linked_link
class Solution(Double_linked_link):
    def delete_all_ocuurance(self,x):
        if self.head.next is None and self.head.val==x:
            return None
        temp=self.head
        prevs=None
        while temp is not None:
            if temp.val==x:
                if prevs is not None:
                    prevs.next=temp.next
                if temp.next is not None:
                    temp.next.prev=prevs
                if temp==self.head:
                    self.head=self.head.next
                    if self.head:
                        self.head.prev = None
                    temp = self.head
                    continue
            else:
                prevs=temp
            temp=temp.next
            
        return self.head

s=Solution()
s.append(2)
s.append(78)
s.append(2)
s.append(75)
s.append(2)
s.append(67)
s.traversal()
print()
x=2
s.delete_all_ocuurance(x)
s.traversal()