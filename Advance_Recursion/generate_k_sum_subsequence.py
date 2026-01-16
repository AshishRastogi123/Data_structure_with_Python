"""
Find all subsequences with sum equals to K
"""
class Solution:
    
    def brute_force(self,nums,target):
        empty=[]
        result=[]
        def solve(index,subset):
            if index>=len(nums):
                if sum(subset)==target:
                #take copy because result array store memory reference 
                    result.append(subset.copy())
                return
            
            # pick the element
            subset.append(nums[index])
            solve(index+1,subset)

            # not pick the element
            subset.pop()
            solve(index+1,subset)
        solve(0,empty)
        return result
    
    def optimal(self,nums,target):
        result=[]
        def solve(index,total,subset):
            if total==target:
                result.append(subset.copy())
                return
            elif total>target:
                return
            if index>=len(nums):
                return
            subset.append(nums[index])
            sum=total+nums[index]
            solve(index+1,sum,subset)
            e=subset.pop()
            sum=sum-e
            solve(index+1,sum,subset)

        solve(0,0,[])
        return result



    
s=Solution()
nums=[5,9,3,4,1]
target=9
p=s.optimal(nums,target)
print(p)