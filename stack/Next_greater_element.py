"""
Next greater element 

Link : https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.
"""
class Next_Greater:
    def brute_force(self,arr):
        """
        Time Complexity : O(N^2)==O(N(N+1)/2)
        Space Complexity : O(N)
        """
        ans=[-1]*len(arr)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    ans[i]=arr[j]
                    break
        return ans
    #Monotonic stack
    def optimal(self,arr):
        """
        Time Complexity : O(2N)
        Space Complexity : O(N)
        """
        ans=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=arr[i]:
                stack.pop()
            if len(stack)!=0:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans


s=Next_Greater()
arr=[1, 3, 2, 4]
print(s.optimal(arr))