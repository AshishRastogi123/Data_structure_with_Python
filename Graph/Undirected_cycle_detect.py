"""
Undirected Graph Cycle
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Note: The graph can have multiple component.

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
"""
from collections import deque
class Solution:
    def cycle_detect_bfs(self,V,E,edges):
        """
        Time Complexity : O(N + 2E)
        Space Complexity : O(N + N + N if need)
        """
        adj_list=[[] for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited=[0]*V
        
        for i in range(V):
            if visited[i]==1:
                continue
            queue=deque()
            queue.append((i,-1))
            visited[i]=1
            while len(queue)!=0:
                node, parent=queue.popleft()
                for adjNode in adj_list[node]:
                    if visited[adjNode]==0:
                        visited[adjNode]=1
                        queue.append((adjNode, node))
                    else:
                        if adjNode!=parent:
                            return True
        return False
s=Solution()
V = 4
E = 4
edges= [[0, 1], [0, 2], [1, 2], [2, 3]]
print(s.cycle_detect_bfs(V,E,edges))