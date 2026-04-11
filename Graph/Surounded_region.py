"""
130. Surrounded Regions

link : https://leetcode.com/problems/surrounded-regions/description/

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""
from collections import deque
class Solution:


    def surrounded_region(self, board):
        """
        Failed at 36 test case because this apporch not work when O are dependent
        """
        row=len(board)
        col=len(board[0])
        queue=deque()
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    queue.append((i,j))
        while len(queue)!=0:
            p,q=queue.popleft()
            left=False
            right=False
            top=False
            bottom =False
            for i in range(col):
                if board[p][i]=='X' and i<q:
                    left=True
                if board[p][i]=='X' and i>q:
                    right=True
                if left==right==True:
                    break
            for j in range(row):
                if board[j][q]=='X' and j<p:
                    top=True
                if board[j][q]=='X' and j>p:
                    bottom=True
                if top==bottom == True:
                    break
            if top==bottom==left==right==True:
                board[p][q]='X'
        print(board)

#===========================================================================================================
    
    def solve(self,board):
        """
        Time Complexity: O(r*c)+ O(r*c*4)+ O(r*c)= O(r*c*4)
        Space Complexity:  O(r*c) stack space
        """
        rows=len(board)
        cols=len(board[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,rows,cols,visited,board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and visited[i][j]==0:
                    board[i][j]='X'
        print(board)

    def dfs(self,r,c,rows, cols, visited,board):
        if r<0 or c<0 or r>=rows or c>=cols:
            return
        if board[r][c]=='X':
            return
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs(r-1,c,rows,cols,visited,board)
        self.dfs(r,c-1,rows,cols,visited,board)
        self.dfs(r+1,c,rows,cols,visited,board)
        self.dfs(r,c+1,rows,cols,visited,board)

#===============================================================================================================

    def more_optimal(self,board):
        """
        Time Complexity : O(4*r*c)
        Space Complexity: O(r*c)
        """
        rows=len(board)
        cols=len(board[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]

        # Upper row
        r,c=0,0
        for c in range(cols):
            if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,rows,cols,visited,board)
        # Last row
        r,c=rows-1,0
        for c in range(cols):
            if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,rows,cols,visited,board)
        # First column
        r,c=0,0
        for r in range(rows):
            if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                           self.dfs(r,c,rows,cols,visited,board)
        # Last column
        r,c=0,cols-1
        for r in range(rows):
            if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,rows,cols,visited,board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and visited[i][j]==0:
                    board[i][j]='X'
        print(board)


            

s=Solution()
board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
print(s.more_optimal(board))