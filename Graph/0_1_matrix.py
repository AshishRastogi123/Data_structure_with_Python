"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from collections import deque
class Solution:
    def zero_one_matrix(self,mat):
        """
        Time Complexity : O(n*m*4)
        Space Complexity: O(2*m*n)
        """
        row=len(mat)
        col=len(mat[0])
        visited=[[0 for i in range(col)] for j in range(row)]
        distance=[[0 for i in range(col)] for j in range(row)]
        queue=deque()
        
        for r in range(row):
            for c in range(col):
                if mat[r][c]==0:
                    queue.append((r,c,0))
                    visited[r][c]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            distance[i][j]=d
            for x,y in [[-1,0],[1,0],[0,-1],[0,1]]:
                new_i,new_j=i+x,j+y
                if new_i<0 or new_i>=row or new_j<0 or new_j>=col:
                    continue
                if visited[new_i][new_j]==1:
                    continue
                queue.append((new_i,new_j,d+1))
                visited[new_i][new_j]=1
        return distance

s=Solution()
mat=[[0,0,0],[0,1,0],[1,1,1]]
print(s.zero_one_matrix(mat))