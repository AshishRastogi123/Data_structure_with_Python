"""
Implement stack and queue using doubly linked list
link: https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.top=None

    def is_Empty(self):
        if self.top==None:
            return True
        return False
    
    def push(self,x):
        new_node=Node(x)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.top==None:
            return -1
        pop_element=self.top.data
        self.top=self.top.next
        return pop_element
    
    def peek(self):
        if self.top==None:
            return -1
        return self.top.data
    
    def size(self):
        if self.top==None:
            return 0
        else:
            count=1
            head=self.top
            while head.next is not None:
                count+=1
                head=head.next
            return count
        

s=Stack()
s.push(67)
s.push(89)
s.push(90)
print(s.peek())
print(s.is_Empty())
print(s.size())
s.pop()
s.pop()
print(s.peek())
print(s.size()
      )

    
