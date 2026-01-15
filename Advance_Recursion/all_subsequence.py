"""
let nums=[9.5,7]
make an recursion tree where apply on all element pick or not pick
got 2^n subsequence
"""



class Solution:
    
    def all_subsequence(self,nums):
        empty=[]
        result=[]
        def solve(index,subset):
            if index>=len(nums):
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
  
    

s=Solution()
nums=[9,5,7]
p=s.all_subsequence(nums)
print(p)