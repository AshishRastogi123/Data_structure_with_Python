"""
Impliment the stack and perform insert, delete , top , size
"""
    
class myStack:
    """
    all takes time complexity : O(1)
    because we used stack list to insert or delete a element at last
    """
    def __init__(self, n):
        self.items=[]
        self.size=n

    
    def isEmpty(self):
        return len(self.items)==0
    
    def isFull(self):
        return len(self.items)==self.size

    
    def push(self, x):
        if self.isFull():
            return False
        return self.items.append(x)


    
    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop() 


    
    def peek(self):
         if self.isEmpty():
            return -1
         return self.items[-1]
    
    def show_stack(self):
        print(self.items)
s=myStack(5)
s.push(2)
s.push(7)
s.push(90)
s.show_stack()
s.pop()
s.show_stack()
print(s.peek())
print(s.isFull())
print(s.isEmpty())