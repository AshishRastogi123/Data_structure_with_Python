"""
Rat maze Problem 

Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).
The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.

Note: Return the final result vector in lexicographically smallest order

Input: maze[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDR
"""
class Solution:
    def rat_maze(self,matrix):
        n=len(matrix)
        ans=[]
        visit=[[0 for _ in range(n)] for _ in range(n)]
        if matrix[0][0]==1:
            self.findpath_helper(0,0,matrix, n, ans, "", visit)
        return ans
    
    def findpath_helper(self, row, col, matrix, n, ans, move, visit):
        if row==n-1 and col==n-1:
            ans.append(move)
            return

        #DownWord
        if row +1 < n and not visit[row+1][col] and matrix[row+1][col]==1:
            visit[row][col]=1
            self.findpath_helper(row+1, col, matrix, n , ans, move + "D",visit)
            visit[row][col]=0

        #Left
        if col-1>=0 and not visit[row][col-1] and matrix[row][col-1]==1:
            visit[row][col]=1
            self.findpath_helper(row, col-1, matrix,n,ans,move + "L",visit)
            visit[row][col]=0

        #Right
        if col+1<n and not visit[row][col+1] and matrix[row][col+1]==1:
            visit[row][col]=1
            self.findpath_helper(row, col+1, matrix, n, ans, move + "R", visit)
            visit[row][col]=0
        #upward
        if row-1>=0 and not visit[row-1][col] and matrix[row-1][col]==1:
            visit[row][col]=1
            self.findpath_helper(row-1,col,matrix,n, ans, move + "U",visit )
            visit[row][col]=0

s=Solution()
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(s.rat_maze(maze))