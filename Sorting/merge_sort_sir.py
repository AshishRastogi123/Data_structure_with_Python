"""
sort an array by merge sort 
"""

arr=[3,1,2,4,1,5,2,6,4]

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge_arrays(left,right)

def merge_arrays(left,right):
    merged=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    while i<len(left):
        merged.append(left[i])
        i+=1
    while j<len(right):
        merged.append(right[j])
        j+=1
    return merged

sorted_arr=merge_sort(arr)
print(sorted_arr)