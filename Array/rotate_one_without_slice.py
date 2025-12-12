arr=[5,-2,3,9,0,10,7]
last=arr[-1]
for i in range(len(arr)-1,-1,-1):
        arr[i]=arr[i-1]
arr[0]=last
print(arr)