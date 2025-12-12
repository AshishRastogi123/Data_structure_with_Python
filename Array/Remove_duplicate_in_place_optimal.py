"""
remove duplicates from a sorted array in place.

here list are sorted already
"""
nums=[0,0,1,1,1,2,2,3,3,4]
#return 0

k=1
for i in range(1,len(nums)):
        if len(nums)==0:
            print(0) 
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k=k+1
print(nums)
print(k-1)
