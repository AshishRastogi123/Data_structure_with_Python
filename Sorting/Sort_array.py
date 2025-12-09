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
start=0
end =8


def reverse_array(arr, start, end):
    if start==end:
        print(arr)
        return 
    p=start
    while p<end:
      if arr[start]>arr[p+1]:
         arr[start],arr[p+1]=arr[p+1],arr[start]
      p+=1

    reverse_array(arr,start+1,end)
reverse_array(arr,start,end)
    
