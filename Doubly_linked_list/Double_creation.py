"""
Double linked list created here
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class Double_linked_link:
    def __init__(self):
        self.head=None
        self.tail = None

    def insert_at_head(self,val):
        """
        Time Complexity : O(1)
        
        """
        new_node=Node(val)
        if not self.head:
            self.head=self.tail=new_node
            return
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def append(self,val):
        """
       Time Complexity : O(n)
       space Complexity : O(1)
        """
        new_node=Node(val)
        if not self.head:
            self.head=self.tail=new_node
            
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            new_node.prev=current
            self.tail=new_node
    def append_using_tail(self,val):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        new_node=Node(val)
        if not self.head:
            self.head=self.tail=new_node
            return
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node


    def insert_at_position(self,val,pos):
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        new_node=Node(val)
        if pos==0:
            self.insert_at_head(val)
            return 
        current=self.head
        count=0
        while current and count<pos:
            current=current.next
            count+=1
        
        if current is None:
            print("Element not Found")

        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node

    def traversal(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next

    def delete_at_head(self):
        if not self.head:
            print("Linked list is empty")
            return
        if self.head==self.tail:
            self.head=self.tail=None
            return
        self.head=self.head.next
        self.head.prev=None
        
    def delete_at_pos(self,pos):
        if not self.head:
            print("Linked list is empty")
            return
        if pos==0:
            self.delete_at_head()
            return
        current=self.head
        count=0
        while current and count<pos:
            current=current.next
            count+=1
        if current is None:
            print("position not present")
            return
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        if current.prev:
            current.prev.next = current.next


    def delete_at_last(self):
        if not self.head:
            print("link list is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail=self.tail.prev
        self.tail.next=None
        
# n1=Node(78)
# n2=Node(64)
# n3=Node(89)
# n4=Node(43)
# n1.next=n2
# n2.prev=n1
# n2.next=n3
# n3.prev=n2
# n3.next=n4
# n4.prev=n3     
if __name__=="__main__":
    d=Double_linked_link()
    # d.insert_at_head(87)   
    # d.insert_at_head(78)  
    # d.insert_at_head(14)  
    # d.insert_at_head(90)  
    # d.insert_at_head(34)  
    d.append(45)
    d.append(78)
    d.append(89)
    d.append(75)
    d.append(34)
    d.append(67)
    d.traversal()
    print()
    d.delete_at_pos(3)
    d.traversal()