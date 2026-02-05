"""
225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.
 The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

 leetcode : https://leetcode.com/problems/implement-stack-using-queues/description/
"""

from collections import deque
class MyStack:

    def __init__(self):
        self.queue=deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        if len(self.queue)==0:
            return -1
        return self.queue.popleft()
        

    def top(self) -> int:
        if len(self.queue)==0:
            return -1
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False