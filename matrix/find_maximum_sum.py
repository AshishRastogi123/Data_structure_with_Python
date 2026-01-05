"""
Docstring for matrix.find_maximum_sum
link: https://leetcode.com/problems/maximum-matrix-sum/

1975. Maximum Matrix Sum
Medium
Topics
premium lock icon
Companies
Hint
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

yaha streagy ye h ki most important line Choose any two adjacent elements of matrix
and multiply each of them by -1 don't care its row or column element find the minimum sum 
so here approach is if we have total negative is even then we can flip all the sign so it became positive so add all elemnet as absolute value

if element is odd then need to substract one but previously we add that element as an odd number so need to substract 2*minabs
we chose minabs because we want max so substract minimum

"""
class Solution:
    def find_maximum(self,matrix):
        total = 0
        negCount = 0
        minAbs = float('inf')

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    negCount += 1
                minAbs = min(minAbs, abs(val))

        if negCount % 2 == 0:
            return total
        else:
            return total - 2 * minAbs

matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
s=Solution()
print(s.find_maximum(matrix))