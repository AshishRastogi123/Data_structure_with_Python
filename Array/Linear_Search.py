"""
nums=[5,3,9,8,1,6,4,-10,-100]
target=4
find the index of target

nums=[10,3,9,10,10,6,4,-10,-100]
target=10
return first index of target

nums=[5,3,9,8,1,6,4,-10,-100]
target=7
return -1 if target not found
"""
class Solution:
    def linearsearch(self,nums,target):
        for i in range(len(nums)):
            if nums[i]==target:
                print(i)
                return i
        print("not present")
            
        return -1
s=Solution()
nums=[5,3,9,8,1,6,4,-10,-100]
target=4
s.linearsearch(nums,target)
