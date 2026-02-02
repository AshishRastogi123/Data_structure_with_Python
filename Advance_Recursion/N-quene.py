"""
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

link : https://leetcode.com/problems/n-queens/description/
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""
class Solution:

    def brute_force(self,n):
        """
        Time Complexity : O(N! x N)
        Space Complexity : O(N^2)
        """
        ans=[]
        board= ["."*n for _ in range(n)]
        self.solve(0,board, ans , n)
        return ans
    def solve(self,col,board, ans , n):
        if col==n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row,col, board,n):
                board[row]= board[row][:col]+ 'Q' +board[row][col+1:]
                self.solve(col+1, board, ans, n)
                board[row]=board[row][:col] + '.' + board[row][col+1:]
    

    def isSafe(self,row, col, board,n):
        duprow=row
        dupcol=col

        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            col-=1
            row-=1

        row=duprow
        col=dupcol

        while col>=0:
            if board[row][col]=='Q':
                    return False
            col-=1

        col=dupcol
        row=duprow

        while row<n and col>=0:
            if board[row][col]=='Q':
                return False
            col-=1
            row+=1

        return True
    
    # Optimal Solution 

    def optimal(self, n):
        """
        Time Complexity : O(N!)
        Space Complexity : O(N)
        """
        ans=[]
        board=['.'*n for _ in range(n)]
        left_row=[0]*n
        upper_diagonal=[0]*(2*n-1)
        lower_diagonal=[0]*(2*n-1)
        self.solution(self,0,board,ans,left_row, upper_diagonal, lower_diagonal,n)
        return ans
    
    def solution(self, col, board,ans,left_row, upper_diagonal, lower_diagonal,n):
        if col==0:
            ans.append(board)
            return True
        for row in range(n):
            if left_row[row]==0 and upper_diagonal[n-1 + col -row]==0 and lower_diagonal[row+col]==0:
                board[row]=board[row][:col] + 'Q' + board[row][col+1:]
                left_row[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[n-1 + row +col]=1
                self.solution( col, board,ans,left_row, lower_diagonal, upper_diagonal, n)
                board[row]=board[row][:col] +'Q' + board[row][col+1:]
                left_row[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[n-1 + row +col]=1

    
    
s=Solution()
print(s.optimal(4))