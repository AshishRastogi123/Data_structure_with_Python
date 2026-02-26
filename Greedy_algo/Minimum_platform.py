"""
Minimum platform
Link : https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.
"""
class Platform:
    def minimum_platform(self,arr,dep):
        ans=1
        for i in range(len(dep)):
            count=1
            for j in range(len(dep)):
                if i != j:
                    if arr[i] < dep[j] and arr[j] < dep[i]:
                        count += 1
            ans=max(count,ans)
        return ans
    
    def optimal(self,arr,dep):
        arr.sort()
        dep.sort()
        ans=1
        count=1
        i=1
        j=0
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            ans=max(ans,count)
        return count
    
p=Platform()
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(p.minimum_platform(arr,dep))