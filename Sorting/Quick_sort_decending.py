"""
sort an array with quick sort

"""
nums=[4,1,2,3,6,7,8,5]
low=0
high=len(nums)-1
def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while i<high and nums[i]>=pivot:
            i+=1
        while j>low and nums[j] < pivot:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        p_index=partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

quick_sort(nums,low,high)
print(nums)