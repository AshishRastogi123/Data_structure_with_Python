arr=[5,-2,3,9,0,10,7]
last=arr[-1]
for i in range(len(arr)-1,0,-1):
        print(i)
        arr[i]=arr[i-1]
arr[0]=last
print(arr)

"""
time complexity: O(n*k)
space complexity: O(1)"""