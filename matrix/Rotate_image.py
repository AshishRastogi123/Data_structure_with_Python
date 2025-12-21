"""
Rotate an 2d  by 90 degree 
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

link= https://leetcode.com/problems/rotate-image/description/
"""

class Solution:
    def brute_force(self,matrix): 
        """
        Time Complexity : O(n^2)
        Space Complexity : O(n^2)
        """
        p=[]
        n=len(matrix)
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(matrix[i][j])
            p.append(row)
        for i in range(n):
            for j in range(n):
                matrix[i][j]=p[len(matrix)-j-1][i]   
    def optimal(matrix):
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
    
s=Solution
matrix = [[1,2,3],[4,5,6],[7,8,9]]

s.optimal(matrix)
print(matrix)