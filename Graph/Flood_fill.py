"""
733. Flood Fill
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]


"""
from collections import deque
class Solution:
    def flood_fill_using_dfs(self,image, sr, sc,color):
        """
        Time Complexity: O(n*m*4)
        Space Complexity: O(n*m) + O(n*m) stack space in case of all need to change the color and a image copy matrix
        """
        if image[sr][sc]==color:
            return image
        image_copy=image.copy()
        rows=len(image)
        cols=len(image[0])
        initial_color=image_copy[sr][sc]
        self.dfs_flood(sr,sc,color,initial_color,image_copy,rows,cols)
        return image_copy

    def dfs_flood(self,i,j,color,initial_color,image_copy,rows,cols):
        if i<0 or i>=rows or j<0 or j>=cols:
            return 
        if image_copy[i][j]!=initial_color:
            return
        if image_copy[i][j]==color:
            return
        image_copy[i][j]=color
        self.dfs_flood(i+1,j,color,initial_color,image_copy,rows,cols)
        self.dfs_flood(i,j+1,color,initial_color,image_copy,rows,cols)
        self.dfs_flood(i-1,j,color,initial_color,image_copy,rows,cols)
        self.dfs_flood(i,j-1,color,initial_color,image_copy,rows,cols)

    def flood_fill_using_bfs(self,image,sr,sc,color):
        """
        Time Complexity : O(n*m*4)
        Space Complexity : O(n*m) +O(n*m)
        """
        if image[sr][sc]==color:
            return image
        image_copy=image.copy()
        rows=len(image)
        cols=len(image[0])
        initial_color=image_copy[sr][sc]
        queue=deque()
        queue.append((sr,sc))
        while queue:
            i,j = queue.popleft()
            image_copy[i][j]=color
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i=i+x
                new_j=j+y
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if image_copy[new_i][new_j]!=initial_color:
                    continue
                queue.append((new_i,new_j))
        return image_copy



s=Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(s.flood_fill_using_bfs(image,sr,sc,color))
