"""
904. Fruit Into Baskets
Link : https://leetcode.com/problems/fruit-into-baskets/description/

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""
class Solution:

    def brute_force(self,fruits):  
        n=len(fruits)
        """
        Got TLE Error 
        Time Complexity : O(n^2)
        Space Complexity : O(1)
        """
        maxi=0
        for i in range(n):
            my_set=set()
            for j in range(i,n):
                my_set.add(fruits[j])
                if len(my_set)>2:
                    break  
                maxi=max(maxi,j-i+1)
        return maxi
    
    def better(self,fruits):
        """
        Time COmplexity : O(2n)
        Space COmplexity : O(1)
        """
        maxi=left=right=0
        n=len(fruits)
        my_dict={}
        while right<n:
            my_dict[fruits[right]]=my_dict.get(fruits[right],0)+1
            while len(my_dict)>2:
                my_dict[fruits[left]]=my_dict[fruits[left]]-1
                if my_dict[fruits[left]]==0:
                    my_dict.pop(fruits[left])
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1

        return maxi
    
    def optimal(self,fruits):
        """
        Time COmplexity : O(2n)
        Space COmplexity : O(1)
        """
        maxi=left=right=0
        n=len(fruits)
        my_dict={}
        while right<n:
            my_dict[fruits[right]]=my_dict.get(fruits[right],0)+1
            if len(my_dict)>2:
                my_dict[fruits[left]]=my_dict[fruits[left]]-1
                if my_dict[fruits[left]]==0:
                    my_dict.pop(fruits[left])
                left+=1
            if len(my_dict)<=2:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi


    

s=Solution()
fruits=[1,2,3,2,2]
print(s.optimal(fruits))