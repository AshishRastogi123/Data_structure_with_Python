"""
Docstring for Linked_list.py.Find_length_of_loop

Link : https://www.geeksforgeeks.org/problems/find-length-of-loop/1


Input: pos = 2,
Output: 4
Explanation: There exists a loop in the linked list and the length of the loop is 4.
"""
from node_creation import Singly_linked_list, Node

class Solution(Singly_linked_list):
    """
       Time Complexity : O(n)
       Space Complexity : O(n) or O(1)
        """
    def brute_force_my(self):
        temp=self.head
        my_dict={}
        travel=0
        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]
            
            my_dict[temp]=travel
            travel+=1
            temp=temp.next
        return 0

    def brute_force1(self):
        """
       Time Complexity : O(n)
       Space Complexity : O(n)
        """
        temp=self.head
        my_set=set()
        while temp is not None:
            if temp in my_set:
                cycle=temp
                break
            my_set.add(temp)
            temp=temp.next
        else:
            return 0
        count=1
        curr=cycle.next
        while curr!=cycle:
            count+=1
            curr=curr.next
        return count
    
    def optimal(self):
        """
       Time Complexity : O(n)
       Space Complexity : O(1)
        """
        s=self.head
        f=self.head
        while f is not None and f.next is not None:
            s=s.next
            f=f.next.next
            if f==s:
                s=s.next
                break
        else:
            return 0

        count=1
        while s!=f:
            s=s.next
            count+=1
            
        return count






m=Solution()
m.appends(87)
m.appends(90)
m.appends(23)
m.appends(67)
m.appends(14)
m.appends(53)
print(m.traversal())