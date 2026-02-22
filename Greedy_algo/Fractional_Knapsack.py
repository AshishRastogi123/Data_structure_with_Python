"""
Fractional Knapsack
link : https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
Output: 240.000000
Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240

Input: val[] = [500], wt[] = [30], capacity = 10
Output: 166.670000
Explanation: Since the item’s weight exceeds capacity, we take a fraction 10/30 of it, yielding value 166.670000.
"""
class Solution:
    def fractional_knapsack(self,val,wt,capacity):
        """
        Greedy Algorithm

        Time Complexity : O(nlog(n)
        space Complexity : O(n)
        """
        arr=[]
        total_val=0.0
        for i in range(len(val)):
            arr.append((val[i]/wt[i],val[i],wt[i]))
        #python me sorting 1 st index ke basis per hoti h agar nested h to 
        # arr.sort(key=lambda x: x.value / x.weight, reverse=True) we can also use that one
        arr.sort(reverse=True)
        for ratio,value,weight in arr:
            if capacity>=weight:
                total_val+=value
                capacity-=weight
            else:
                total_val+=ratio*capacity
                break
        return total_val
        

    
s=Solution()
val= [60, 100, 120]
wt= [10, 20, 30]
capacity = 50
print(s.fractional_knapsack(val,wt,capacity))