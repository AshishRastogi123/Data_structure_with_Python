"""
Reverse an array using recursion where you have two variable left and right and sort the array between them
let left =2, right=9 and not interfare another 

num=[5,1,9,12,5,8,4,19,10]
left =2
right =5
then output
[5,1,4,5,8,9,12,19,10]


"""

arr=[5,1,9,12,5,8,4,19,10]
left=0
right =8

def reverse_array(arr,left,right):
    if left >=right:
        print(arr)
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_array(arr,left+1,right-1)
reverse_array(arr,left,right)
