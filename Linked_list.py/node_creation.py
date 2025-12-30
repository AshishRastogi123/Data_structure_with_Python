"""
Node creation and linked it of linked list
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
node1=Node(7)
node2=Node(92)
node3=Node(83)
node4=Node(71)

print(node1)# when we try to print an object we got address of the object
print(node1.val)
node1.next=node2
node2.next=node3
node3.next=node4

print(node1.next.val)
print(node1.next.next.next.val)
