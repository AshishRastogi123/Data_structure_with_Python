"""
455. Assign Cookies

link : https://leetcode.com/problems/assign-cookies/description/
Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""
class Solution:
    def findContentChildren(self,g,c):
          """
          Time complexity : O(nlog(n))
          Space Complexity : O(1)
          """
          count=left=right=0
          g.sort()
          c.sort()
          while left<len(g) and right<len(c):
               if g[left]<=c[right]:
                    count+=1
                    left+=1

               right+=1

          return count

p=Solution()
g = [1,2]
s = [1,2,3]
print(p.findContentChildren(g,s))
                