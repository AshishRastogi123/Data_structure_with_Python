"""
Node creation and linked it of linked list
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Singly_linked_list:
    def __init__(self):
        self.head=None
    
    def appends(self,data):
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
                print(curr.val, end=" ")
                curr=curr.next
    
# node1=Node(7)
# node2=Node(92)
# node3=Node(83)
# node4=Node(71)

# print(node1)  when we try to print an object we got address of the object
# print(node1.val)
# node1.next=node2
# node2.next=node3
# node3.next=node4

# print(node1.next.val)
# print(node1.next.next.next.val)
s=Singly_linked_list()
s.appends(25)
s.appends(97)
s.appends(12)
s.appends(76)
print(s.traversal())