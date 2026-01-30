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
class SOlution:
    def brute_force(self,n):
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
    
s=SOlution()
print(s.brute_force(4))