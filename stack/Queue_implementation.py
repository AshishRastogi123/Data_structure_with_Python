"""
Docstring for stack.Queue_implementation
"""

class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.items=[]
        self.n=n

    
    def isEmpty(self):
        # Check if queue is empty
        if len(self.items)==0:
            return True
        return False

    
    def isFull(self):
        # Check if queue is full
        if len(self.items)==self.n:
            return True
        return False


    
    def enqueue(self, x):
        # Enqueue
        if len(self.items)==self.n:
            return "Queue is full"

        self.items.append(x)

    
    def dequeue(self):
        # Dequeue
        if len(self.items)==0:
            return -1

        self.items.pop(0)

    
    def getFront(self):
        # Get front element
        if len(self.items)==0:
            return -1
        return self.items[0]
       
    
    def getRear(self):
        # Get rear element
        if len(self.items)==0:
            return -1
        
        return  self.items[-1]
        
s=myQueue(5)
s.enqueue(12)
s.enqueue(78)
s.enqueue(34)
s.enqueue(44)
s.getFront()
s.getRear()
s.isEmpty()
s.isFull()
s.dequeue()
s.dequeue()
print(s.items)