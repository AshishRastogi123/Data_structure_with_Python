"""
perform insertion sort on a list of numbers
"""
nums=[3,5,1,8,7,2,4,6,0,9,11,10]
l=len(nums)
for i in range(1,l):
    key =nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)
    