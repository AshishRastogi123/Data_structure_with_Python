"""
Impliment the stack and perform insert, delete , top , size
"""
class Stack:
    """
    all takes time complexity : O(1)
    because we used stack list to insert or delete a element at last
    """
    def __init__(self):
        self.items=[]

    def insert(self,item):
        self.items.append(item)

    def delete(self):
        self.items.pop()

    def size(self):
        return len(self.items)
    
    def top(self):
        if len(self.items)==0:
            return "Stack is Empty"
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items)==0
    
    def show_stack(self):
        print(self.items)
s=Stack()
s.insert(2)
s.insert(7)
s.insert(90)
s.show_stack()
s.delete()
s.show_stack()
print(s.top())
print(s.size())
print(s.is_empty())