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
                print(curr.val, end=" ")
                curr=curr.next

    def inserts(self,val,position):
        """
        Time Complexity : O(n)
        space Complexity : O(1)
        """

        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current is not None and count<position:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current

        
    def delete_at_start(self):
        temp=self.head
        self.head=self.head.next
        #now traversal or another can not reach 1st one because head shifted 
        temp.next=None
        del temp
    
    def delete_based_value(self,val):
        curr=self.head
        if curr.next is not None:
            if curr.next==val:
                self.head=curr.next
                return
            else:
                found=False
                prev=None
                while curr is not None:
                    if curr.val==val:
                        found=True
                        break
                    prev=curr
                    curr=curr.next
                if found:
                    prev.next=curr.next
                    return
                else:
                    print("node not found")



    
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
s.inserts(67,2)
print(s.traversal())
s.delete_based_value(12)
print(s.traversal())