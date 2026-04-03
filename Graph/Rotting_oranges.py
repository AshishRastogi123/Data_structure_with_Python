"""
994. Rotting Oranges

link: https://leetcode.com/problems/rotting-oranges/description/
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
"""
from collections import deque
class Solution:
    def rotting_oranges(self,grid):
        """
        Time COmplexity : O(r*c)+ O(r*c*4)=O(r*c*4)
        Space Complexity : O(r*c)+O(r*c)=O(r*c)
        """
        rows=len(grid)
        cols=len(grid[0])
        grid_copy=grid.copy()

        queue=deque()
        fress_count=0

        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c]==2:
                    queue.append((r,c))
                elif grid_copy[r][c]==1:
                    fress_count+=1
        minutes=0

        while len(queue)!=0 and fress_count>0:
            minutes+=1
            total_rotten=len(queue)
            for _ in range(total_rotten):
                i,j=queue.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i, new_j= i+dx, j+dy
                    if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                        continue
                    if grid_copy[new_i][new_j]==0 or grid_copy[new_i][new_j]==2:
                        continue
                    fress_count-=1
                    grid_copy[new_i][new_j]=2
                    queue.append((new_i,new_j))
        if fress_count>0:
            return -1
        return minutes
    
s=Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.rotting_oranges(grid))



