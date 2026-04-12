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
class Solution:
    def Number_of_envlave(self,grid):
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


s=Solution()
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s.Number_of_envlave(grid))      
