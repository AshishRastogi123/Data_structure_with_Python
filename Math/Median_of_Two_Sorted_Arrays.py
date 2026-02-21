"""
Median of the sorted array
Link : https://leetcode.com/problems/median-of-two-sorted-arrays/

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
import statistics
class Solution:
    def Smart(self,nums1,nums2):
        """
        Time Complexity : O((m+n) log(m+n))
        space Complexity  : O(m+n)
        This will not safe
        """
        return statistics.median(sorted(nums1+nums2))
    def my_solution(self,nums1,nums2):
        """
        Time Complexity : O((m+n) log(m+n))
        space Complexitys : O(m+n)
        """
        merge=sorted(nums1+nums2)
        n=len(merge)
        if n%2==1:
            return merge[n//2]
        else:
            return (merge[n//2-1]+merge[n//2])/2
    
s=Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.my_solution(nums1,nums2))