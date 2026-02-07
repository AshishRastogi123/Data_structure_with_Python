"""
Implement Queue using 2 stack 

link : https://leetcode.com/problems/implement-queue-using-stacks/description/

"""
class Solution:

    def __init__(self):
        self.sh1=[]
        self.sh2=[]
        

    def push(self, x: int) -> None:
        while self.sh1:
            self.sh2.append(self.sh1.pop())
        
        self.sh1.append(x)
        while self.sh2:
            self.sh1.append(self.sh2.pop())
        

        
        

    def pop(self) -> int:
         if not self.sh1:
             return -1
         return self.sh1.pop()
        

    def peek(self) -> int:
        if not self.sh1:
            return -1
        return self.sh1[-1]
        

    def empty(self) -> bool:
        if len(self.sh1)==0:
            return True
        return False
    
class MyQueue:

    def __init__(self):
        self.sh1=[]
        self.sh2=[]
        

    def push(self, x: int) -> None:
        if len(self.sh1)<=2 :
            self.sh1.append(x)
            return
        
        for i in self.sh1:
            self.sh2.append(i)
        self.sh1.clear()
        for i in range(len(self.sh2)):
            self.sh1.append(self.sh2[i])
        self.sh2.clear()
        self.sh1.append(x)

        
        

    def pop(self) -> int:
         return self.sh1.pop(0)
        

    def peek(self) -> int:
        return self.sh1[0]
        

    def empty(self) -> bool:
        if len(self.sh1)==0:
            return True
        return False
        
    
s=Solution()
s.push(30)
s.push(40)
s.push(50)
print(s.sh1)
s.pop()
print(s.sh1)
print(s.peek())
print(s.empty())
s.pop()
print(s.peek())
print(s.sh1, s.sh2)