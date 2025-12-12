nums = [-1,0,0,0,0,3,3]
k={}
for i in range(0,len(nums)):
            if nums[i] not in k:
                k[nums[i]]=0


l=list(k.keys())
for j in range(len(l)):
        nums[j]=l[j]
#got error on leetcode because of this
#dictionary does not maintain order
                


print(k)
print(nums)
                