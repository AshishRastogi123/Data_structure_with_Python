"""
1020. Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Link : https://leetcode.com/problems/number-of-enclaves/description/

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
"""
from collections import deque
class Solution:
    def Number_of_envlave(self,grid):
        """
        Time Complexity : O(r*c*4)
        Space Complexity : O()
        """
        rows=len(grid)
        cols=len(grid[0])
        count=0
        r,c=0,0
        for c in range(cols):
                if grid[r][c]==1:
                    self.dfs(r,c,rows,cols,grid)
        r,c=rows-1,0
        for c in range(cols):
            if grid[r][c]==1:
                self.dfs(r,c,rows,cols,grid)
        r,c=0,0
        for r in range(rows):
                if grid[r][c]==1:
                    self.dfs(r,c,rows,cols,grid)
        r,c=0,cols-1
        for r in range(rows):
                if grid[r][c]==1:
                    self.dfs(r,c,rows,cols,grid)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count+=1
        return count

    def dfs(self,r,c,rows,cols,grid):
        if r<0 or r>=rows or c<0 or c >=cols:
            return
        if grid[r][c]==0:
            return
        grid[r][c]=0
        self.dfs(r-1,c,rows,cols,grid)
        self.dfs(r,c-1,rows,cols,grid)
        self.dfs(r+1,c,rows,cols,grid)
        self.dfs(r,c+1,rows,cols,grid)

#-------------------------------Using Bfs---------------------------------------------------------

    def Number_using_bfs(self,grid):
         """
         Time Complexity : O(m*n) + O(4*m*n)
         Space Complexity : O(m*n)+ O(m*n)
         """
         rows=len(grid)
         cols=len(grid[0])
         queue=deque()
         visited=[[0 for _ in range(cols)] for _ in range(rows)]
         count=0
         for r in range(rows):
              for c in range(cols):
                   if r==0 or c==0 or r==rows-1 or c==cols-1:
                        if grid[r][c]==1:
                             queue.append((r,c))
                             visited[r][c]=1
        
         while len(queue)!=0:
              i,j=queue.popleft()
              for x , y in [(-1,0),(0,-1),(1,0),(0,1)]:
                   new_i,new_j=i+x,j+y
                   if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols-1:
                        continue
                   if grid[new_i][new_j]==0:
                        continue
                   if grid[new_i][new_j]==0 or visited[new_i][new_j]==1:
                        continue
                   queue.append((new_i,new_j))
                   visited[new_i][new_j]=1
                
         for i in range(rows):
              for j in range(cols):
                   if grid[i][j]==1 and visited[i][j]==0:
                        count+=1
         return count
                        



s=Solution()
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s.Number_using_bfs(grid))      
