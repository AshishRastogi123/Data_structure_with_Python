"""
Find pairs with given sum in doubly linked list

link : https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs 
(1, 6) and (2,5) with sum 
"""
from Double_creation import Double_linked_link
class Solution(Double_linked_link):
    def brute_force(self,target):
        """
        Time Complexity : O(n**2)
        Space Complexity : O(n) or O(1)
        """
        first=self.head
        l=[]
        while first:
            second=first.next
            while second:
                if first.val+second.val==target:
                    l.append([first.val,second.val])
                second=second.next
            first=first.next
        return l
    
    def better(self,target):
        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        first=self.head
        my_set=set()
        result=[]
        while first:
            remaining=target-first.val
            if remaining in my_set:
                result.append([remaining,first.val])
            my_set.add(first.val)
            first=first.next
        return result
    
    def optimal(self,target):
        right=self.head
        left=self.head
        result=[]
        while right.next:
            right=right.next
        while left and right and left.val<right.val:
            if left.val+right.val>target:
                right=right.prev
                continue
            if left.val+right.val==target:
                result.append([left.val,right.val])
                right=right.prev
            left=left.next
            
        return result
    
    def sir_solution(self,target):
        right=self.head
        left=self.head
        result=[]
        while right.next:
            right=right.next
        while left and right and left.val<right.val:
            if left.val+right.val==target:
                result.append([left.val,right.val])
                left=left.next
                right=right.prev
            elif left.val+right.val>target:
                right=right.prev
            else:
                left=left.next
        return result
            
            







            
s=Solution()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.append(8)
s.append(9)
p=s.sir_solution(7)
print(p)





