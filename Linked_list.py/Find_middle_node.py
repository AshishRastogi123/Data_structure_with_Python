"""
Find middle node of linkedlist if number of nodes is even then have two middle return second one

Link= https://leetcode.com/problems/middle-of-the-linked-list/description/


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Middle_element:
    def __init__(self):
        self.head=None
    
    def append(self,val):
        """
       Time Complexity : O(n)
       Space Complexity : O(1)
        """
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node

    def traversal(self):
        if self.head==None:
            print("link list is empty")
        else:
            curr=self.head
            while curr!=None:
                print(curr.val, end=" -> ")
                curr=curr.next
        
    
    def miiddle_brute(self):
        temp=self.head
        n=0
        while temp is not None:
            n+=1
            temp=temp.next
        
        temp=self.head
        for i in range(n//2):
            temp=temp.next

        return temp.val

    def middle_optimal(self):
        """
        TORTOISE - HARE algo
        Time Complexity : O(n/2) 
        Space Complexity : O(1)
        here we have 2 pointers where 1st is slow which run normal speed and fast run 2x speed of s then when fast visit whole linked list slow are exact mid
        """
        s=self.head
        f=self.head
        
        while f and f.next:
            s=s.next
            f=s.next.next
        return s.val
        





m=Middle_element()
m.append(87)
m.append(90)
m.append(23)
m.append(67)
m.append(14)
m.append(53)
print(m.traversal())
print(m.middle_optimal())
