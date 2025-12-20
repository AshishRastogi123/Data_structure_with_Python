"""
73. Set Matrix Zeroes
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
class Solution:
    def brute_force(self,matrix:list[list[int]])->None:
        """
        Time complexity: O(n*m(n+m))+O(n*m)
        Space complexity: O(1)
        """
        
        def marK_infinity(matrix,row,col):
            r=len(matrix)
            c=len(matrix[0])
            for i in range(r):
                 if matrix[i][col]!=0:
                    matrix[i][col]=float("inf")
            for j in range(c):
                if matrix[row][j]!=0:
                    matrix[row][j]=float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    marK_infinity(matrix,i,j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0
    def optimal(self,matrix:list[list[int]])->None:
        """
        time complexity: O(n*m)
        space complexity: O(n+m)=O(n)
        """
        r=len(matrix)
        c=len(matrix[0])
        rowtrack=[0 for _ in range(r)]
        coltrack=[0 for _ in range(c)]
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    coltrack[j]=-1
        for i in range(0,r):
            for j in range(0,c):
                if rowtrack[i]==-1 or coltrack[j]==-1:
                    matrix[i][j]=0



s=Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.optimal(matrix)
print(matrix)