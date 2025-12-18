"""
Best time to buy an stock 

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
class Solution:
    def stock_buy_sell(self,price):
        minimum=float("inf")
        maxi=float("-inf")
        for i in range(len(price)):
            if minimum>price[i]:
                p=i
                minimum=price[i]
        for j in range(p,len(price)):
            if price[j]>maxi:
                maxi=price[j]
        return maxi-minimum
            

prices = [7,1,5,3,6,4]
s=Solution()
n=s.stock_buy_sell(prices)  
print(n)        
