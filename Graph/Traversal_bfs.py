"""
Traversal using breath first search

Link : 
"""
from collections import deque
class Solution:
    def breath_first_search(self,adj):
        """
        Space Complexity: O(3n)
        Time Complexity : O(n + 3e)
        """
        ans=[]
        queue=deque()
        n=len(adj)
        start=1
        visited=[0]*n
        queue.append(start)
        visited[start]=1
        while len(queue):
            e=queue.popleft()
            ans.append(e)
            for node in adj[e]:
                if visited[node]==0:
                    queue.append(node)
                    visited[node]=1
        return ans
s=Solution()
n = 9

adjacency_list = [
    [],
    [2, 8],
    [1, 3, 4],
    [2],
    [2, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [1, 7, 9],
    [8],
]

print(s.breath_first_search(adjacency_list))