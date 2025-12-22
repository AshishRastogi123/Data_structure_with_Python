"""
Make matrix in sprial order
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Link= https://leetcode.com/problems/spiral-matrix/description/
"""
class Solution():
    def brute_force(self,matrix):
        n=len(matrix)
        p=0
        k=0
        m=[]
        for i in range(n):
            if p==0:
                for j in range(n):
                
                    m.append(matrix[i][j])
                p+=1
            if p==1:
                for j in range(i+1,n):
                    m.append(matrix[j][n-1-i])
                p+=1
            if p==2:
                for j in range(i+1,n):
                    m.append(matrix[n-i-1][n-j-1])
                p+=1
            if p==3:
                k+=1
                for j in range(i+1,n):
                    if j==n-1:
                        continue
                    m.append(matrix[n-j-1][i])
                p+=1
            if p==4:
                pass 
        print(m)
    def optimal(self,matrix):
        if not matrix or not matrix[0]:
            return []
        result=[]
        top,left=0,0
        bottom,right=len(matrix)-1,len(matrix[0])-1

        #run the loop until all boudary will not left
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom-=1
            if left <=right:
                for i in range(bottom,top -1, -1):
                    result.append(matrix[i][left])
                left+=1
        return result
    
s=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=s.optimal(matrix)
print(n)