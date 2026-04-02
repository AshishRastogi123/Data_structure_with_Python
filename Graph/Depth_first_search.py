"""
link : https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

"""
class Solution:

    def only_one_based_first_search(self,adj):
        """
        Time Complexity: O(n)+ O(2E) number of degrees
        Space Complexity: O(2n) + O(n) number of vertex
        """
        ans=[]
        visited = [0] * (len(adj) + 1)
        self.solve(1, visited, ans, adj)
        return ans
        
    def solve(self,node,visited,ans,adj):
        visited[node]=1
        ans.append(node)
        for n in adj[node]:
            if visited[n]==0:
                self.solve(n,visited,ans,adj)
        
    def both_based_graph(self,adj):
        """
        Time Complexity: O(n)+ O(2E) number of degrees
        Space Complexity: O(2n) + O(n) number of vertex
        """
        ans = []
        visited = [0] * len(adj)
        
        for i in range(len(adj)):   # handle disconnected graph
            if visited[i] == 0:
                self.solve(i, visited, ans, adj)
        
        return ans

s=Solution()
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

print(s.only_one_based_first_search(adjacency_list))
