"""
Reverse a Linked list 
link = https://leetcode.com/problems/reverse-linked-list/description/

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
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

    def Reverse_brute(self):
        """
        Time COmplexity : O(n)
        space Complexity : O(1)
        """
        temp=self.head
        stack=[]
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=self.head

        while temp is not None:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return self.head
    
    def optimal(self):
        temp=self.head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front 
        return prev

s=Singly_linked_list()
s.appends(78)
s.appends(97)
s.appends(26)
s.appends(65)
s.appends(12)
s.traversal()
# s.Reverse_brute()
# print("\nAfter Reverse")
s.traversal()
s.optimal()
print("Optimal Solution")
s.traversal()
