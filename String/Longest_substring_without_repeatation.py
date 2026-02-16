"""
3. Longest Substring Without Repeating Characters

Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
"""
class Solution:
    
    def brute_force(self,s):
        """
        Time Complexity : O(n(n+1)/2) or O(n^2)
        Space Complexity : O(n)
        """
        maxi=0
        my_set=set()
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in my_set:
                    break
                my_set.add(s[j])
            if len(my_set)>maxi:
                maxi=len(my_set)
            my_set.clear()
        return maxi
    
    def optimal(self,s):
        """
        using sliding window and two pointers
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        my_dist={}
        left=right=maxi=0
        while right<len(s):
            if s[right] in my_dist:
                left=max(left, my_dist[s[right]]+1)
            maxi=max(maxi,right-left+1)
            my_dist[s[right]]=right
            right+=1
        return maxi

    
s=Solution()
p = "abcabcbb"
print(s.optimal(p))