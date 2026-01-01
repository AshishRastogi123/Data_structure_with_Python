"""
Find where cycle started 
Link :https://leetcode.com/problems/linked-list-cycle-ii/description/

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
"""

from node_creation import  Singly_linked_list

class Solution(Singly_linked_list):
    def brute_force(self):
        temp=self.head
        my_set=set()
        while temp is not None:
            if  temp in my_set:
                return temp
            my_set.add(temp)
            temp=temp.next
        return None
    
    def optimal_my_not(self):
        s=self.head
        f=self.head
        kn=False
        while f is not None and f.next is not None:
            if f==s:
                if kn==True:
                    return f
                kn=True
                s=self.head

            if kn==False:       
                s=s.next
                f=f.next.next
            else:
                s=s.next
                f=f.next
        return None
    
    def optimal(self):
        """
        Time Complexity : O(n)
        space Complexity : O(1)
        """
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:           # it work agar if loop khatam hone se phele nhi chala or agar if chala then skip this
            return None  

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow






p=Singly_linked_list()
p.appends(102)
p.appends(89)
p.appends(12)
p.appends(56)
p.traversal()
s=Solution()
s.optimal()