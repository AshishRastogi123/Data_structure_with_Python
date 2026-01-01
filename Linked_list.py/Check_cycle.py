"""
141. Linked List Cycle (Floyd's Cycle detection)
Find in the linked list an cycle present or not

Link: https://leetcode.com/problems/linked-list-cycle/description/
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

"""
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class Singly_linked_list:
    def __init__(self):
        self.head=None
    
    def appends(self,data):
        """
       Time Complexity : O(n)
       Space Complexity : O(1)
        """
        new_node=Node(data)
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
    def cycle_detection(self):
        """
        Time COmplexity : O(n)
        Space Complexity : O(n)
        """
        temp=self.head
        my_set=set()
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp=temp.next
        return False
    
    def optimal_cycle(self):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        s=self.head
        f=self.head
        while f is not None and f.next is not None:
            s=s.next
            f=f.next
            if s==f:
                return True
        return False
    # Find 
            
s=Singly_linked_list()
s.appends(25)
s.appends(97)
s.appends(12)
s.appends(76)
print(s.traversal())

