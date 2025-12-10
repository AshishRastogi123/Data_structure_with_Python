"""
sort an array using Bubble_sort
"""
n=[3,5,1,8,7,2,4,6,0,9,11,10]
p=len(n)
for i in range(p-2,-1,-1):
    for j in range(0,i+1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]

print(n)

"""
Here the time complexity is : o(n(n+1)/2) =o(n^2) for best / worst and average case
"""