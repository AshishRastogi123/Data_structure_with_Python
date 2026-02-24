"""
860. Lemonate change

Link : https://leetcode.com/problems/lemonade-change/description/

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
"""
class Solution:
     def lemonadeChange(self, bills):
        my_dict = {20: 0, 10: 0, 5: 0}
        l = [10, 5]          # change sirf 10 aur 5 se
        price = 5

        for i in range(len(bills)):
            curr = bills[i] - price

            # pehle change do
            j = 0
            while j < len(l):
                if curr == 0:
                    break

                if l[j] > curr or my_dict[l[j]] == 0:
                    j += 1
                else:
                    my_dict[l[j]] -= 1
                    curr -= l[j]

            if curr != 0:
                return False

            # ab customer ka bill add karo
            my_dict[bills[i]] += 1

        return True
     

     def Sir_solution(self,bills):
          n=len(bills)
          five=0
          ten=0
          for i in range(n):
               if bills[i]==5:
                    five+=1
               elif bills[i]==10:
                    
                    if five>=1:
                        five-=1
                        ten+=1
                    else:
                         return False
               else:
                    if five>=1 and ten>=1:
                         five-=1
                      
                         ten-=1
                    elif five>=3:
                         five-=3
                    else:
                         return False
          return True
                    
               

s=Solution()
bills=[5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(s.Sir_solution(bills))
