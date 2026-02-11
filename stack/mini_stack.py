"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


"""
class MiniStack:
    def __init__(self):
        self.items=[]

    def push(self, val):
        if len(self.items)==0:
            self.items.append([val,val])
        else:
            mini=min(self.items[-1][1],val)
            self.items.append([val,mini])

    def pop(self):
        if len(self.items)==0:
            return -1
        return self.items.pop()

    def top(self):
        if len(self.items)==0:
            return -1
        return self.items[-1][0]

    def getmini(self):
        if len(self.items)==0:
            return 0
        return self.items[-1][1]

s=MiniStack()
print(s.push(90))
print(s.push(20))
print(s.push(50))
print(s.getmini())
print(s.top())
print(s.pop())
print(s.getmini())