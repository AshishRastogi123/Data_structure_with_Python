"""
queue implementation using linked list

Link : https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1
"""
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def is_Empty(self):
        return self.rear is None
    
    def enqueue(self,x):
        new_data=Node(x)
        if self.rear==None:
            
            self.rear=self.front=new_data
            return

        self.rear.next=new_data
        self.rear=new_data
        
    def dequeue(self):
        if self.rear is None:
            return -1
        pop_element=self.front.data
        self.front=self.front.next

        if self.front is None:
            self.rear=None
        return pop_element
    
    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data
    
    def size(self):
        head=self.front
        count=0
        while head is not None:
            count+=1
            head=head.next
        return count

q=Queue()
print(q.is_Empty())

q.enqueue(78)
q.enqueue(90)
q.enqueue(89)
print(q.is_Empty())
q.dequeue()
print(q.size()) 
q.dequeue()
print(q.getFront())

