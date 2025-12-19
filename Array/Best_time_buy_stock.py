"""
Best time to buy an stock 

Input: pricess = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (prices = 1) and sell on day 5 (prices = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
class Solution:
    def stock_buy_sell(self,prices):
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        minimum=float("inf")
        maxi_profit=0
        for i in range(len(prices)):
            if minimum>prices[i]:
                minimum=prices[i]
            if (prices[i]-minimum)>maxi_profit:
                maxi_profit=prices[i]-minimum
        return maxi_profit
    """
    failed at 154 case out 212 test
    """
    def Brute_force(self,pricess):
        """
        Time complexity:o(n*n)
        """
        maxi=float("-inf")
        for i in range(len(pricess)):
                for j in range(i+1,len(pricess)):
                    if pricess[i]<pricess[j]:
                        p=pricess[j]-pricess[i]
                        maxi=max(maxi,p)

        return maxi
    
  

pricess = [2,4,1]
s=Solution()
n=s.stock_buy_sell(pricess)  
print(n)        
