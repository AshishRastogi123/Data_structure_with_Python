"""
204. Count Primes

link: https://leetcode.com/problems/count-primes/

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def count_prime(self,n):
        """
        Not Accepted TLE error
        Time Complexity: O(n^2))
        Space Complexity : O(1)
        """
        if n<=2:
            return 0
        count=1
        mila=True
        for i in range(3,n,2):
            for j in range(3,i,2):
                    if i%j==0 :
                        mila=False
                        break
            if mila:
                count+=1
            mila=True
        return count
    
    def Optimal(self,n):
         """
         Sieve of Eratosthenes (O(n log log n))Instead of checking every number individually, we mark multiples of primes as non-prime.
        Create a boolean list is_prime, Assume all numbers are prime initially, Start from 2, Mark multiples as False, Count remaining True values
         """
         if n<=2:
              return 0
         is_prime=[True]*n
         is_prime[0]=is_prime[1]=False
         p=2
         while p*p<n:
              if is_prime[p]:
                   for i in range(p*p,n,p):
                        is_prime[i]=False
              p+=1
         return sum(is_prime)

s=Solution()

print(s.count_prime(10))

                
            